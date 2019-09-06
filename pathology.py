# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#
# Pathology implementation from
# https://code.tutsplus.com/tutorials/#how-to-write-package-and-distribute-a-library-in-python--cms-28693
#
# Also available as pip install pathology
#
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import pathlib
import inspect

class Path(type(pathlib.Path())):
    @staticmethod
    def script_dir():
        print(inspect.stack()[1].filename)
        p = pathlib.Path(inspect.stack()[1].filename)
        return p.parent.resolve()