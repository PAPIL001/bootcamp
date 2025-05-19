import requests
import logging
from config import BIOC_API_BASE_URL  # We might still use this later
from config import PUBTATOR3_BASE_URL_PMC_EXPORT  # Define this new config

logger = logging.getLogger(__name__)

def fetch_bioc_xml(pmc_id: str) -> str | None:
    """
    Fetches the BioC XML content for a given PMC ID from the NCBI API (original method).
    """
    url = f"{BIOC_API_BASE_URL}?format=xml&id={pmc_id}"
    logger.info(f"Fetching BioC XML for PMC ID: {pmc_id} from URL: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching BioC XML for PMC ID {pmc_id}: {e}")
        return None

def fetch_pubtator3_biocxml_pmc(pmc_id: str) -> str | None:
    """
    Fetches BioC XML content from PubTator3 using the pmc_export endpoint.

    Args:
        pmc_id: The PubMed Central identifier (e.g., "PMC123456").

    Returns:
        The BioC XML content as a string, or None if an error occurs.
    """
    url = f"{PUBTATOR3_BASE_URL_PMC_EXPORT}?pmcids={pmc_id}"
    logger.info(f"Fetching BioC XML from PubTator3 for PMC ID: {pmc_id} from URL: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching BioC XML from PubTator3 for PMC ID {pmc_id}: {e}")
        return None