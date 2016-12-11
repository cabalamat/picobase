# doc.py = A Document

"""***
A Doc contains a document that can be put in a table.

Keys are strings, values are any Jsonable value.

***"""

from picotypes import *

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
    
    def satisfies(self, query: Query)-> bool:
        """ Does this document satisfy a query ? """
        if query is None: return True
        for k, v in query.items():
            if self.hasattr(k) and self.__dict__[k]==v:
                pass
            else:
                return False
        #//for
        return True
    
    
    
#---------------------------------------------------------------------

# end