import copy
import math

import numpy as np

class GeometryBase():
    """
    Base class for geometry classes
    """

    def __init__(self, source):
        """
        Constructor
        """

        self.xml_schema = ''

        if isinstance(source, type(self)):
            self.copy_source(source)

            self._key_pairs = {}

    def __str__(self):
        """
        String representation
        """

        return str(self.__dict__)

    def getv(self, key):
        """
        Generic getter for class attributes
        """

        assert (key in self.__dict__()),\
            "Invalid key {} accessing arc {}".format(key, self.id)

        return getattr(self, self._key_pairs[key])

    def setv(self, key, value):
        """
        Generic setter for class attributes
        """

        _keys = list(self.__dict__.keys())

        if not key in _keys:

            assert (set([key]).issubset(set(self._key_pairs))),\
                "Invalid key {} accessing arc {}".format(key, self.id)


            key = _keys[self._key_pairs.index(key)]

        setattr(self, key, value)

    def copy_source(self, source):
        """
        Copy the source object to the targer
        """

        if isinstance(source, self):
            self.__dict__ = copy.deepcopy(source.__dict__)
            self._key_pairs = source._key_pairs.copy()
            return

        #build a list of key pairs fir string-based lookup
        self._key_pairs = {}

        _keys = list(self.__dict__.keys())

        for _i, _k in enumerate(self._key_pairs):
            self._key_pairs[_k] = _keys[_i]

        if isinstance(source, dict):
            for _k, _v in source.items():
                self.setv(_k, _v)

    def to_dict(self):
        """
        Return the object as a dictionary
        """

        _result = {}

        _result.update(
            [(_k, getattr(self, _v)) for _k, _v in self._key_pairs.items()])

        return _result

    def validate_as_vector(self, data):
        """
        Validate the incoming data as a numpy.array vector.
        Convert if in compatible format
        """

        if data is None:
            return None

        if math.isnan(data):
            return None

        _result = data

        if isinstance(data, str):

            _v = data.split(' ')

            assert(len(_v) == 3), 'Expected 3 floats for pi value {}'\
                .format(data)

            for _w in _v:
                assert(float(_w)), 'Non-float value passed for pi value {}'\
                    .format(data)

            _result = np.array([float(_w) for _w in _v])

        elif isinstance(data, list):

            for _v in data:
                assert(float(_w)), 'Non-float value passed for pi value {}'\
                    .format(data)

            _result = np.array(data)

        elif isinstance(data, tuple):

            _result = np.array(data)

        else:

            assert(
                isinstance(data, np.ndarray)), 'Invalid type for pi value {}'\
                .format(data)

        return _result
