from lxml import etree
import logging

logger = logging.getLogger(__name__)

def extract_figure_captions(xml_content: str) -> list[str]:
    """
    Extracts figure captions from BioC XML content from PubTator3.

    Args:
        xml_content: The BioC XML content as a string.

    Returns:
        A list of figure captions (strings).
    """
    captions = []
    try:
        root = etree.fromstring(xml_content.encode('utf-8'))
        for passage in root.xpath('//document/passage'):
            section_type_elements = passage.xpath('./infon[@key="section_type"]')
            if section_type_elements:
                section_type = section_type_elements[0].text
                print(f"Section Type: {section_type}")
                if section_type.upper() == "FIG":
                    print("Found a FIG passage")
                    text_elements = passage.xpath('./text')
                    if text_elements:
                        text_element = text_elements[0]
                        caption_text = text_element.text
                        if caption_text:
                            print(f"Extracted Caption Text: {caption_text.strip()}")
                            captions.append(caption_text.strip())
                        else:
                            print("Text element has no text content.")
                    else:
                        print("No text element found in FIG passage.")
                else:
                    print("Not a FIG passage")
            else:
                print("No section_type infon found in passage.")
        print("--- Finished processing passages ---")

    except etree.XMLSyntaxError as e:
        logger.error(f"Error parsing BioC XML: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while extracting captions: {e}")
    return captions

if __name__ == "__main__":
    # Example usage (replace with your sample_pubtator3_pmc_export.xml content)
    sample_xml = """
    <?xml version='1.0' encoding='UTF-8'?><!DOCTYPE collection SYSTEM 'BioC.dtd'><collection><source>PubTator</source><date></date><key>BioC.key</key><document><id>3166167</id><passage><infon key="name_2">surname:Striepen;given-names:Boris</infon><infon key="name_1">surname:DeRisi;given-names:Joseph L.</infon><infon key="name_0">surname:Yeh;given-names:Ellen</infon><infon key="issue">8</infon><infon key="year">2011</infon><infon key="article-id_publisher-id">PBIOLOGY-D-11-01871</infon><infon key="alt-title">Chemical Rescue of Apicoplast-Minus P. falciparum</infon><infon key="article-id_doi">10.1371/journal.pbio.1001138</infon><infon key="type">front</infon><infon key="elocation-id">e1001138</infon><infon key="volume">9</infon><infon key="license">This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.</infon><infon key="section_type">TITLE</infon><infon key="article-id_pmc">3166167</infon><infon key="article-id_pmid">21912516</infon><offset>0</offset><text>Chemical Rescue of Malaria Parasites Lacking an Apicoplast Defines Organelle Function in Blood-Stage Plasmodium falciparum </text><annotation id="22354"><infon key="identifier">5833</infon><infon key="type">Species</infon><location offset="101" length="21" /><text>Plasmodium falciparum</text></annotation><annotation id="22355"><infon key="identifier">MESH:D008288</infon><infon key="type">Disease</infon><location offset="19" length="17" /><text>Malaria Parasites</text></annotation></passage><passage><infon key="section_type">ABSTRACT</infon><infon key="type">abstract</infon><offset>124</offset><text>The only essential function of a unique plastid organelle, the apicoplast, in blood-stage P. falciparum is the production of isoprenoid precursors.</text><annotation id="22356"><infon key="identifier">MESH:D013729</infon><infon key="type">Chemical</infon><location offset="249" length="10" /><text>isoprenoid</text></annotation><annotation id="22357"><infon key="identifier">5833</infon><infon key="type">Species</infon><location offset="214" length="13" /><text>P. falciparum</text></annotation></passage><passage><infon key="section_type">FIG_CAP</infon><offset>12130</offset><text>Figure 1. IPP chemically rescues fosmidomycin inhibition of parasite growth.
(A) Dose-response curves of P. falciparum W2 growth in the presence of fosmidomycin alone (closed circles) or supplemented with 200 µM IPP (open circles), DMAPP (open triangles), or both (open squares). Parasitemia was determined by FACS after 72 h. The EC50 value (± 95% confidence interval) for fosmidomycin alone is shown. Data are representative of three independent experiments.
(B) Dose-response curve of P. falciparum W2 growth in the presence of 100 µM fosmidomycin supplemented with increasing concentrations of IPP. Parasitemia was determined by FACS after 72 h. Data are representative of three independent experiments.</text></passage></document></collection>
    """
    captions = extract_figure_captions(sample_xml)
    if captions:
        print("Extracted Figure Captions:")
        for caption in captions:
            print(f"- {caption}")
    else:
        print("No figure captions found in the XML.")