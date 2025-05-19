# src/ingestion/pubmed_central.py
import requests
import logging
from typing import Optional, List, Dict
from lxml import etree
import urllib.parse

logger = logging.getLogger(__name__)

class PubMedCentralFetcher:
    def __init__(self):
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.pubtator_url = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator"

    def fetch_article_xml(self, pmc_id: str) -> Optional[bytes]:
        """
        Fetches the full XML content of the article from PubMed Central using E-utilities.

        Args:
            pmc_id: The PMC ID of the article (e.g., PMC3535000).

        Returns:
            The XML content as bytes if successful, None otherwise.
        """
        pmc_id_numeric = pmc_id.replace("PMC", "").strip()
        params = {
            'db': 'pmc',
            'id': pmc_id_numeric,
            'rettype': 'native',
            'retmode': 'xml'
        }
        url = f"{self.base_url}efetch.fcgi?{urllib.parse.urlencode(params)}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            xml_content = response.content
            # Save the XML content to a file for inspection
            with open(f"pmc_{pmc_id}_native.xml", "wb") as f:
                f.write(xml_content)
            return xml_content
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching XML for {pmc_id} from PMC via E-utilities: {e}")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred during E-utilities XML fetching: {e}")
            return None

    def extract_entities_from_caption(self, caption: str) -> List[Dict]:
        """
        Attempts to call the PubTator API using a POST request with text in the body.
        """
        headers = {'Content-Type': 'text/plain'}
        try:
            response = requests.post(self.pubtator_url, headers=headers, data=caption.encode('utf-8'))
            response.raise_for_status()

            entities = []
            for line in response.text.strip().split('\n'):
                parts = line.split('\t')
                if len(parts) >= 4:
                    entity_text = parts[3]
                    entity_type = parts[4]
                    if entity_type == "Gene":
                        entities.append({'name': entity_text, 'type': entity_type})
            return entities

        except requests.exceptions.RequestException as e:
            logger.error(f"Error calling PubTator API: {e}")
            return []
        except Exception as e:
            logger.error(f"Error processing PubTator API response: {e}")
            return []

    def extract_article_details_from_xml(self, xml_content: bytes) -> Optional[Dict]:
        """
        Extracts title, abstract, and figure captions from the article XML content.  Also extracts entities.

        Args:
            xml_content: The XML content of the article as bytes.

        Returns:
            A dictionary with 'title', 'abstract', 'figure_captions' (list of strings),
            and 'figure_entities' (dict of caption: list of entities).
            Returns None on error.
        """
        try:
            root = etree.fromstring(xml_content)
            title = root.xpath("//article/front/article-meta/title-group/article-title/text()")
            abstract_parts = root.xpath("//article/front/article-meta/abstract//p/text()")
            abstract = " ".join(abstract_parts) if abstract_parts else None

            caption_elements = root.xpath("//article/body//fig/caption//p/text()")
            figure_captions = [caption.strip() for caption in caption_elements]

            article_details = {
                'title': title[0] if title else None,
                'abstract': abstract,
                'figure_captions': figure_captions,
                'figure_entities': {}  # Store entities per caption
            }

            for caption in figure_captions:
                entities = self.extract_entities_from_caption(caption)
                article_details['figure_entities'][caption] = entities  # Store extracted entities

            return article_details
        except etree.XMLSyntaxError as e:
            logger.error(f"Error parsing XML from E-utilities: {e}")
            with open("malformed_pubmed_xml_eutils.xml", "wb") as f:
                f.write(xml_content)
            return None
        except Exception as e:
            logger.error(f"Error extracting details from XML from E-utilities: {e}")
            return None


if __name__ == "__main__":
    # Example usage
    pmc_fetcher = PubMedCentralFetcher()
    pmc_id_to_test = "PMC7782049"  # PLOS One article with figures
    xml_content = pmc_fetcher.fetch_article_xml(pmc_id_to_test)

    if xml_content:
        article_details = pmc_fetcher.extract_article_details_from_xml(xml_content)
        if article_details:
            print(f"Title: {article_details.get('title')}")
            print(f"Abstract: {article_details.get('abstract')}")
            print("Figure Captions and Entities:")
            for caption, entities in article_details.get('figure_entities', {}).items():
                print(f"- Caption: {caption}")
                if entities:
                    print("  Genes:")
                    for entity in entities:
                        print(f"    - {entity['name']}")  # Only print the gene name
                else:
                    print("  No genes found in this caption.")
        else:
            print(f"Failed to extract details for {pmc_id_to_test} from XML (E-utilities).")
    else:
        print(f"Failed to fetch XML for {pmc_id_to_test} via E-utilities.")