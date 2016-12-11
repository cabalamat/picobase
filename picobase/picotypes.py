# picotypes.py = types used by picobase

from typing import Union, Dict, List, Tuple, Any

#---------------------------------------------------------------------

SimpleValue = Union[str, int, float, bool, None]

""" this is what it should be, but doesn't work:
Jsonable = Union[SimpleValue, 
                 Dict[str, 'Jsonable'], 
                 List['Jsonable'], 
                 Tuple['Jsonable', ...]]
"""
JsonDict = Dict[str, Any]
Jsonable = Union[SimpleValue,
                 JsonDict,
                 List[Any],
                 Tuple[Any, ...]]


"""
Queries are a subset of those in MongoDB and are of the form:

   { fieldName1: value1,
     fieldName2: value2 
     ...
   }

Every field mentioned has to have the specified value.

Later, queries will be more complete. A query of {} or None
passes through all Documents.
"""
Query = Union[Dict[str,Any], None]

"""
An _id (primary key) to a document is either a string or an integer.
"""
IdType = Union[str,int]


#---------------------------------------------------------------------



#end
