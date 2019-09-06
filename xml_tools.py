from lxml import etree

import datetime

def validate_etree(tree, xsd_path):
    """
    Validate an etree object against the provided schema
    """

    _schema = etree.XMLSchema(etree.parse(xsd_path))

    _result = None

    if _schema.validate(tree):
        _result = tree

    return _result

def load_xml(xml_path, xsd_path):
    """
    Load the XML filepath and validate against the schema
    """

    _doc = etree.parse(xml_path)

    return validate_etree(_doc, xsd_path)

def etree_to_dict(node):
    """
    Convert an element tree node to a dictionary
    """

    #Implementation courtesy of StackOverflow user K3---rnc:
    #https://stackoverflow.com/questions/7684333/converting-xml-to-dictionary-using-elementtree

    d = {node.tag: {} if node.attrib else None}

    children = list(node)

    if children:

        dd = {}

        for dc in map(etree_to_dict, children):

            for k, v in dc.items():

                if not k in dd:
                    dd[k] = []

                dd[k].append(v)

        d = {node.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.items()}}

    if node.attrib:
        d[node.tag].update(('@' + k, v) for k, v in node.attrib.items())

    if node.text:

        text = node.text.strip()

        if children or node.attrib:

            if text:
              d[node.tag]['#text'] = text

        else:
            d[node.tag] = text

    return d

def dict_to_etree(d, version):
    """
    Convert an XML dictionary to an element tree
    """

    #Implementation courtesy of StackOverflow user K3---rnc:
    #https://stackoverflow.com/questions/7684333/converting-xml-to-dictionary-using-elementtree

    init_xml(version)

    def _to_etree(d, root):
        if not d:
            pass
        elif isinstance(d, str):
            root.text = d
        elif isinstance(d, dict):
            for k,v in d.items():
                assert isinstance(k, str)
                if k.startswith('#'):
                    assert k == '#text' and isinstance(v, str)
                    root.text = v
                elif k.startswith('@'):
                    assert isinstance(v, str)
                    root.set(k[1:], v)
                elif isinstance(v, list):
                    for e in v:
                        _to_etree(e, etree.SubElement(root, k))
                else:
                    _to_etree(v, etree.SubElement(root, k))
        else:
            assert d == 'invalid type', (type(d), d)
    assert isinstance(d, dict) and len(d) == 1

    _key = list(d.keys())[0]
    if 'LandXML' in _key:
        d = d[_key]

    tag, body = next(iter(d.items()))
    node = etree.Element(tag)
    _to_etree(body, node)
    return etree.ElementTree(node)

def init_xml(version):
    """
    Initialize an XML tree
    """
    _ns = "http://www.landxml.org/schema/LandXML-1.0"
    _xsd = 'http://www.landxml.org/schema/LandXML-1.2/LandXML-1.0.xsd'

    if version == 1.1:
        _ns = "http://www.landxml.org/schema/LandXML-1.1"
        _xsd = 'http://www.landxml.org/schema/LandXML-1.2/LandXML-1.1.xsd'

    elif version == 1.2:
        _ns = "http://www.landxml.org/schema/LandXML-1.2"
        _xsd = 'http://www.landxml.org/schema/LandXML-1.2/LandXML-1.2.xsd'

    LANDXML_NS = _ns
    LANDXML = "{%s}" % LANDXML_NS
    NSMAP = {None: LANDXML_NS,
             'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    }

    _xsi_sl = etree.QName('http://www.w3.org/2001/XMLSchema-instance',
        'schemaLocation'
    )

    _node = etree.Element(LANDXML + "LandXML", {_xsi_sl: 'http://www.landxml.org/schema/LandXML-1.2/LandXML-1.2.xsd'},
    nsmap=NSMAP,
        version=version,
        date=str(datetime.date.today()),
        time=datetime.datetime.now().strftime('%H:%M:%S'),
        readOnly='false',
        language='English',
        )

    return _node

def write_xml(tree, file_path):

    tree.write(
        file_path, encoding='utf-8', xml_declaration=True, pretty_print=True)

def test_xml():

    etree.dump(init_xml('1.2'))