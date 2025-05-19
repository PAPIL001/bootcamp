# src/entity_extractor.py
import requests
import time
import logging

logger = logging.getLogger(__name__)

PUBTATOR3_REQUEST_URL = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/request.cgi"
PUBTATOR3_RETRIEVE_URL = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/retrieve.cgi"

def extract_entities_pubtator3(text, bioconcept=None):
    """
    Extracts entities from the given text using the PubTator3 API (two-step process).

    Args:
        text (str): The text to extract entities from.
        bioconcept (str, optional): The bioconcept type to focus on (e.g., "Gene"). Defaults to None.

    Returns:
        list: A list of dictionaries, where each dictionary represents an entity
              and contains keys like 'text' and 'type'. Returns an empty list
              if there's an error or no entities are found.
    """
    entities = []
    request_params = {'text': text}
    if bioconcept:
        request_params['bioconcept'] = bioconcept

    logger.debug(f"Sending PubTator3 request for text: '{text}'")  # Added debug log

    try:
        # Step 1: Submit request
        request_response = requests.post(PUBTATOR3_REQUEST_URL, data=request_params)
        request_response.raise_for_status()
        session_id = request_response.text.strip()
        logger.info(f"PubTator3 request submitted, session ID: {session_id}")

        # Step 2: Retrieve result with polling
        max_attempts = 10
        wait_time = 5  # seconds
        for attempt in range(max_attempts):
            retrieve_params = {'id': session_id}
            retrieve_response = requests.post(PUBTATOR3_RETRIEVE_URL, data=retrieve_params)

            logger.debug(f"PubTator3 retrieve status code: {retrieve_response.status_code}") # Added debug log
            logger.debug(f"PubTator3 retrieve response text: '{retrieve_response.text}'") # Added debug log

            if retrieve_response.status_code == 200:
                # Process the result (assuming PubTator format for now)
                for line in retrieve_response.text.strip().split('\n'):
                    parts = line.split('\t')
                    if len(parts) >= 5:
                        entity_text = parts[3]
                        entity_type = parts[4]
                        entities.append({'text': entity_text, 'type': entity_type})
                logger.info(f"PubTator3 result retrieved successfully for session ID: {session_id}")
                logger.debug(f"Extracted entities: {entities}") # Added debug log
                return entities
            elif retrieve_response.status_code == 404 and "Result is not ready" in retrieve_response.text:
                logger.warning(f"PubTator3 result not ready yet (attempt {attempt + 1}/{max_attempts}). Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                logger.error(f"Error retrieving PubTator3 result (attempt {attempt + 1}/{max_attempts}): {retrieve_response.status_code} - {retrieve_response.text}")
                return []

        logger.error(f"Max attempts reached while retrieving PubTator3 result for session ID: {session_id}")
        return []

    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with PubTator3 API: {e}")
        return []

if __name__ == '__main__':
    test_caption = "The expression of the EGFR gene was significantly increased in the tumor samples."
    entities = extract_entities_pubtator3(test_caption, bioconcept="Gene")
    print(f"Entities found: {entities}")

    test_caption_multi = "Mutations in BRCA1 and BRCA2 genes increase the risk of breast cancer."
    entities_multi = extract_entities_pubtator3(test_caption_multi)
    print(f"Entities found (multi): {entities_multi}")