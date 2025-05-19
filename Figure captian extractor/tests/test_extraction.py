import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from lxml import etree
from src import extraction
from unittest.mock import patch  # If not using pytest-mock
import requests
# ... rest of your test code ...

# ... rest of your test code ...
# Sample BioC XML content (replace with a snippet from your
# 'sample_pubtator3_pmc_export.xml' that includes a title, abstract, and a figure caption)
SAMPLE_XML = """
<collection>
<document>
<id>3166167</id>
<passage>
<infon key="section_type">TITLE</infon>
<offset>0</offset>
<text>Chemical rescue of malaria parasites lacking an apicoplast defines organelle function in blood-stage Plasmodium falciparum </text>
</passage>
<passage>
<infon key="section_type">ABSTRACT</infon>
<offset>124</offset>
<text>The apicoplast, a plastid organelle essential for the human malaria parasite Plasmodium falciparum, is the target of several promising antimalarial drugs. However, its precise metabolic functions during the erythrocytic stages of parasite development are not fully understood. Here, we show that...</text>
</passage>
<passage>
<infon key="section_type">FIG</infon>
<offset>0</offset>
<text>Chemical rescue of fosmidomycin inhibition with IPP precursors.</text>
</passage>
<passage>
<infon key="section_type">FIG</infon>
<offset>1500</offset>
<text>Western blot analysis of apicoplast protein expression.</text>
</passage>
<passage>
<infon key="section_type">FIG</infon>
<offset>2200</offset>
<text>Fluorescence microscopy of parasite cultures.</text>
</passage>
</document>
</collection>
"""

def test_extract_paper_data_successful():
    extracted_data = extraction.extract_paper_data(SAMPLE_XML)
    assert extracted_data["title"] == "Chemical rescue of malaria parasites lacking an apicoplast defines organelle function in blood-stage Plasmodium falciparum"
    assert extracted_data["abstract"].startswith("The apicoplast, a plastid organelle essential")
    assert len(extracted_data["figure_captions"]) == 3
    assert "Chemical rescue of fosmidomycin inhibition with IPP precursors." in extracted_data["figure_captions"]
    assert "Western blot analysis of apicoplast protein expression." in extracted_data["figure_captions"]
    assert "Fluorescence microscopy of parasite cultures." in extracted_data["figure_captions"]

def test_fetch_bioc_xml_successful(mocker):  # Use 'mocker' if you have pytest-mock
    pmc_id = "PMC1234567"
    sample_xml_content = "<collection><document><id>1234567</id></document></collection>"

    mock_response = mocker.Mock()  # Create a mock Response object
    mock_response.raise_for_status.return_value = None  # Simulate a successful response
    mock_response.text = sample_xml_content

    mocker.patch('requests.get', return_value=mock_response)  # Mock requests.get

    fetched_xml = extraction.fetch_bioc_xml(pmc_id)
    assert fetched_xml == sample_xml_content

def test_fetch_bioc_xml_error(mocker, caplog):  # Use 'mocker' if you have pytest-mock, 'caplog' for capturing logs
    pmc_id = "PMC9876543"
    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("API error")

    mocker.patch('requests.get', return_value=mock_response)

    fetched_xml = extraction.fetch_bioc_xml(pmc_id)
    assert fetched_xml is None
    assert f"Error fetching XML from PubTator3 for PMC ID {pmc_id}" in caplog.text