# doc.py = A Document

"""***
A Doc contains a document that can be put in a table.

Keys are strings, values are any Jsonable value.

***"""

from typing import Union, Dict, List, Tuple

SimpleValue = Union[str, int, float, bool, None]

Jsonable = Union[SimpleValue, 
                 Dict[str, 'Jsonable'], 
                 List['Jsonable'], 
                 Tuple['Jsonable', ...]]

JsonDict = Dict[str, 'Jsonable']

import json

v = [2,3,4, "hello", (66,77), True, None]
j = json.dumps(v)

print("v=%r\nj=%r" % (v,j))

#---------------------------------------------------------------------

class Doc:

    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self):
        keys = sorted(self.__dict__.keys())
        args = ["%s=%r" % (key, self.__dict__[key])
                for key in keys]
        return 'Doc(%s)' % ', '.join(args)

    def hasattr(self, key: str) -> bool:
        return key in self.__dict__
    
    def value(self) -> JsonDict:
        return self.__dict__
    
    def hasId(self) -> bool:
        """ does this document have an _id? """
        return '_id' in self.__dict__
    
    
    
    
#---------------------------------------------------------------------

# end