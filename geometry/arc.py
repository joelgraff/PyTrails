import math

from .geometry_base import GeometryBase

class Arc(GeometryBase):
    """
    Arc class object
    """

    _xml_keys = [
        'name', 'type', 'Start', 'End', 'PI', 'Center', 'dirStart',
        'dirEnd', 'length', 'staStart', 'staInternal', 'delta',
        'rot', 'tangent', 'radius', 'chord', '_middle', 'midOrd',
        'external', 'desc', 'state', 'oID', 'note', '_points', 'crvType'
    ]

    def __init__(self, source=None):
        """
        Arc class constructor
        """

        self.id = ''
        self.type = 'Arc'
        self.start = None
        self.end = None
        self.pi = None
        self.center = None
        self.bearing_in = math.nan
        self.bearing_out = math.nan
        self.length = 0.0
        self.start_station = 0.0
        self.internal_station = 0.0
        self.delta = 0.0
        self.direction = 0.0
        self.tangent = 0.0
        self.radius = 0.0
        self.chord = 0.0
        self.middle = 0.0
        self.middle_ordinate = 0.0
        self.external = 0.0
        self.description = ''
        self.status = ''
        self.object_id = ''
        self.note = ''
        self.points = []
        self.xml_crvType = 'arc'
        self.__pi = None
        self.__start = None
        self.__end = None
        self.__center = None
        self.__bearing_in = None
        self.__bearing_out = None

        super().__init__(source)

        self._key_pairs = Arc._xml_keys

    def setv(self, key, value):
        print('\n\tarc setv', key, value)
        super().setv(key, value)

    def __str__(self):
        """
        Stringification
        """

        _result = ''
        for _k, _v in self.__dict__.items():

            _key = _k

            if _key == '_key_pairs':
                continue

            if _key.startswith('_Arc_'):
                _key = _key[6:]

            _result += _key + ':' + str(_v) + '\n'

        return _result

    @property
    def pi(self):
        """
        PI property getter
        """
        return self.__pi

    @pi.setter
    def pi(self, pi):
        """
        PI property setter
        """

        self.__pi = self.validate_as_vector(pi)

    @property
    def start(self):
        """
        Start point property getter
        """
        return self.__start

    @start.setter
    def start(self, start):
        """
        Start point property setter
        """

        self.__start = self.validate_as_vector(start)

    @property
    def center(self):
        """
        Center point property getter
        """
        return self.__center

    @center.setter
    def center(self, center):
        """
        Center point property setter
        """

        self.__center = self.validate_as_vector(center)

    @property
    def end(self):
        """
        End point property getter
        """
        return self.__end

    @end.setter
    def end(self, end):
        """
        End point property setter
        """

        self.__end = self.validate_as_vector(end)

    @property
    def bearing_in(self):
        """
        End point property getter
        """
        return self.__bearing_in

    @end.setter
    def bearing_in(self, bearing_in):
        """
        End point property setter
        """

        self.__bearing_in = self.validate_as_vector(bearing_in)

    @property
    def bearing_out(self):
        """
        End point property getter
        """
        return self.__bearing_out

    @end.setter
    def bearing_out(self, bearing_out):
        """
        End point property setter
        """

        self.__bearing_out = self.validate_as_vector(bearing_out)

    def to_etree(self):
        """
        Convert the object to the equivalent etree
        """

        pass
