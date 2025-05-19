from lxml import etree
import requests
import logging
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

BIOC_PMC_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/REST/pmc/getBioC/PMC{pmc_id}/xml"
PUBTATOR3_API_URL = "https://pubtator.ncbi.nlm.nih.gov/api/ner?passages={text}&concept={concept}"

def fetch_bioc_xml(pmc_id: str) -> Optional[bytes]:
    """
    Fetches the full XML content for a given PMC ID using NCBI E-utilities.
    """
    print(f"Fetching full XML for PMC ID via E-utilities: {pmc_id}")
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmc_id.lstrip('PMC')}&rettype=xml&retmode=text"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching full XML for PMC ID {pmc_id} via E-utilities from {url}: {e}")
        return None

def extract_paper_data(xml_content: bytes) -> Dict:
    """
    Parses the JATS XML content and extracts relevant information, handling namespaces.
    """
    try:
        root = etree.fromstring(xml_content)
        ns = {'xlink': 'http://www.w3.org/1999/xlink'}  # Define the xlink namespace

        title_nodes = root.xpath("//article-meta/title-group/article-title/text()")
        title = " ".join(title_nodes) if title_nodes else None
        abstract_nodes = root.xpath("//article-meta/abstract/p/text()")
        abstract = " ".join(abstract_nodes) if abstract_nodes else None
        figure_captions = []
        figure_elements = root.xpath("//fig")
        for fig in figure_elements:
            caption_nodes = fig.xpath("./caption/p/text()")
            caption_text = " ".join(caption_nodes) if caption_nodes else None
            image_url = None
            graphic_node = fig.xpath("./graphic/@xlink:href", namespaces=ns)
            if graphic_node:
                image_url = graphic_node[0]
            media_node = fig.xpath("./media/@xlink:href", namespaces=ns)
            if media_node:
                image_url = media_node[0]

            if caption_text:
                figure_captions.append({'text': caption_text, 'url': image_url})

        return {"title": title, "abstract": abstract, "figure_captions": [item['text'] for item in figure_captions], "figure_urls": [item['url'] for item in figure_captions]}

    except etree.XMLSyntaxError as e:
        logger.error(f"XML Syntax Error: {e}")
        return {"title": None, "abstract": None, "figure_captions": [], "figure_urls": []}
    except Exception as e:
        logger.error(f"An unexpected error occurred during XML processing: {e}")
        return {"title": None, "abstract": None, "figure_captions": [], "figure_urls": []}

def extract_entities(text: str, concept: str = "gene") -> Optional[List[Dict]]:
    """
    Extracts entities (e.g., genes) from a given text using the PubTator3 API.

    Args:
        text (str): The text to analyze.
        concept (str, optional): The type of concept to extract (e.g., "gene", "disease").
                                Defaults to "gene".

    Returns:
        Optional[List[Dict]]: A list of dictionaries, where each dictionary represents an entity
                                (with 'text', 'start', 'end', 'identifier', 'type').
                                Returns None if an error occurs.
    """
    url = PUBTATOR3_API_URL.format(text=text, concept=concept)
    try:
        response = requests.get(url)
        response.raise_for_status()
        # PubTator3 returns plain text with entities separated by tabs
        entities = []
        for line in response.text.strip().split('\n'):
            parts = line.split('\t')
            if len(parts) >= 5:
                entity = {
                    'text': parts[3],
                    'start': int(parts[1]),
                    'end': int(parts[2]),
                    'identifier': parts[4],
                    'type': parts[5] if len(parts) > 5 else concept
                }
                entities.append(entity)
        return entities
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching entities from PubTator3 for text: '{text}': {e}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred during entity extraction: {e}")
        return None

if __name__ == '__main__':
    # Example usage (for testing extraction logic)
    pmc_id = "PMC3166167"
    xml_content = fetch_bioc_xml(pmc_id)
    if xml_content:
        data = extract_paper_data(xml_content)
        print("Title:", data.get("title"))
        print("Abstract:", data.get("abstract"))
        print("Figure Captions with URLs:")
        for caption, url in zip(data.get("figure_captions", []), data.get("figure_urls", [])):
            print(f"- {caption} (URL: {url})")

        # Example of entity extraction (for one of the captions)
        if data.get("figure_captions"):
            first_caption = data["figure_captions"][0]
            entities = extract_entities(first_caption, concept="gene")
            print("\nEntities in the first caption:")
            if entities:
                for entity in entities:
                    print(f"  - {entity['text']} ({entity['type']})")
            else:
                print("  No entities found.")
