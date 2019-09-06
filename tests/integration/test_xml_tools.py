import pytest

from lxml import etree

from ...pathology import Path

from ...xml_tools import\
    validate_etree, load_xml, etree_to_dict, dict_to_etree, write_xml

xml_file = str(Path.script_dir())+'/../../resources/data/divcibare.xml'
xsd_file = str(Path.script_dir())+'/../../resources/data/LandXML-1.0.xsd'
xml_version = '1.0'

def test_validate_xml():

    tree = etree.parse(xml_file)

    assert validate_etree(tree, xsd_file) is not None

def test_load_xml():

    assert load_xml(xml_file, xsd_file) is not None

def test_etree_to_dict():

    _etree = load_xml(xml_file, xsd_file)

    assert etree_to_dict(_etree.getroot()) is not None

def test_dict_to_etree():

    _etree = load_xml(xml_file, xsd_file)
    _dict = etree_to_dict(_etree.getroot())

    assert dict_to_etree(_dict, xml_version) is not None

def test_write_xml():

    _etree = load_xml(xml_file, xsd_file)
    _dict = etree_to_dict(_etree.getroot())
    _etree = dict_to_etree(_dict, xml_version)
    write_xml(_etree, 'test.xml')

    assert load_xml('test.xml', xsd_file) is not None
