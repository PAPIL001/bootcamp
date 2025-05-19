# src/pubmed_parser.py
import requests
import xml.etree.ElementTree as ET
import logging
from src.entity_extractor import extract_entities_pubtator3

logger = logging.getLogger(__name__)

class PubMedParser:
    def __init__(self, pmc_id):
        self.pmc_id = pmc_id
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

    def fetch_article(self):
        params = {
            'db': 'pmc',
            'id': self.pmc_id,
            'rettype': 'xml',
            'retmode': 'text'
        }
        try:
            response = requests.get(f"{self.base_url}efetch.fcgi", params=params)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching article for {self.pmc_id}: {e}")
            return None

    def parse(self):
        logger.debug(f"Entering parse method for PMC ID: {self.pmc_id}")
        xml_content = self.fetch_article()
        if xml_content:
            logger.debug(f"XML content for {self.pmc_id}:\n{xml_content}") # Print the XML content
            try:
                root = ET.fromstring(xml_content)
                article = {}
                title_element = root.find('.//article-title')
                article['title'] = ''.join(title_element.itertext()) if title_element is not None else None
                abstract_elements = root.findall('.//abstract/p')
                article['abstract'] = '\n'.join([''.join(p.itertext()) for p in abstract_elements]) if abstract_elements else None
                article['pmc'] = self.pmc_id
                article['pmid'] = root.findtext('.//article-id[@pub-id-type="pmid"]')
                figure_captions = []
                fig_elements = root.findall('.//fig') # Try relative path first
                if not fig_elements:
                    fig_elements = root.findall('fig') # Try direct children
                    if not fig_elements:
                        fig_elements = list(root.iterfind('fig')) # Iterate through all descendants
                logger.debug(f"Number of <fig> elements found (after broader search): {len(fig_elements)}")
                for fig in fig_elements:
                    caption_element = fig.find('caption/p')
                    url_element = fig.find('.//graphic')
                    caption_text = ''.join(caption_element.itertext()) if caption_element is not None else None
                    figure_url = url_element.get('{http://www.w3.org/1999/xlink}href') if url_element is not None else None
                    entities = []
                    if caption_text:
                        logger.debug(f"Found caption text: '{caption_text}'")
                        logger.debug(f"Parsing caption text: '{caption_text}' for entities")
                        entities = extract_entities_pubtator3(caption_text)
                        logger.debug(f"Extracted entities for this caption: {entities}")
                    figure_captions.append({'caption': caption_text, 'url': figure_url, 'entities': entities})
                article['figure_captions'] = figure_captions
                return article
            except ET.ParseError as e:
                logger.error(f"Error parsing XML for {self.pmc_id}: {e}")
                return None
        return None

if __name__ == '__main__':
    parser = PubMedParser('PMC1234567')
    data = parser.parse()
    if data and data.get('figure_captions'):
        for caption_data in data['figure_captions']:
            print(f"Caption: {caption_data['caption']}")
            print(f"Entities: {caption_data['entities']}")
    elif data:
        print(data)
    else:
        print("Failed to parse data.")