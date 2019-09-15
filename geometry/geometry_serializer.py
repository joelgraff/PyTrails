import xml_tools

from geometry.arc import Arc

def deserialize(xml_path, xsd_path):
    """
    Construct corresponding geometry from a LandXML file
    """

    _tree = xml_tools.load_xml(xml_path, xsd_path)

    assert (_tree is not None),\
        {"Invalid element tree from file {} and schema {}"\
            .format(xml_path, xsd_path)}

    _data = xml_tools.etree_to_dict(_tree.getroot())

    assert (_data is not None),\
        {"Invalid dictionary from file {} and schema {}"\
            .format(xml_path, xsd_path)}

    _structure = {}

    #return structre containing the objects constructed from dictionary
    recurse_dict(_data, _structure)

def recurse_dict(data, structure, level=0):
    """
    Recurse a LandXML data dictionary, building
    """

    if isinstance(data, dict):

        for x in data:

            if level == 0:

                if x[0] == '{':

                    _text = x.split('}')

                    if _text[1] == 'LandXML':
                        structure['schema'] = _text[0] + '}'

            elif structure['schema'] in x:

                _key = x.split('}')[1]

                #if a curve tag, a single-element list follows with the
                #requisite curve data
                if 'Curve' in _key:

                    _data = data[x]

                    if isinstance(_data, list):
                        _data = _data[0]

                    structure[_key] = build_curve(_data)

            recurse_dict(data[x], structure, level + 1)

    elif isinstance(data, list):

        for x in data:
            recurse_dict(x, structure, level + 1)

def serialize(data):
    """
    Serialize the geometry data structure into a LandXML file
    """

    pass

def build_curve(data):
    """
    Build a curve object from the passed XML data set
    """

    _arc = Arc()

    for _k in data:

        if _k[0] == '{':
            _arc.setv(_k.split('}')[1], data[_k])

        elif _k[0] == '@':
            _arc.setv(_k[1:], data[_k])

    return _arc

def _deser():

    deserialize('/home/joel/Projects/PyTrails/resources/data/SugarGroveRd.xml', '/home/joel/Projects/PyTrails/resources/data/LandXML-1.2.xsd')