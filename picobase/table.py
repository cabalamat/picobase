# table.py = a Table in a Database


from typing import *

from database import Database
from doc import Doc

#---------------------------------------------------------------------

"""
Queries are a ssubset of those in MongoDB and are of the form:

   { fieldName1: value1,
     fieldName2: value2 
     ...
   }

Every field mentioned has to have the specified value.

Later, queries will be more complete. A query of {} or None
passes through all Documents.
"""
Query = Union[Dict[str,Any], None]


class Table:
    
    def __init__(self, db: Database, name: str)->None:
        self.name = name
        self.db = db
        self.docs = [] # type: List[Doc]
        self.index = {} # type: Dict[str, Doc]
        self.nextId = 1 # type: int
        
    def addDoc(self. doc: Doc) -> None:
        """ Adds a document to this table. 
        gives it an _id if need be.
        """
        if doc.hasId():
            if doc._id in self.index:
                self.removeDoc(doc._id)           
        else:
            doc._id = self.newId()          
        self.docs = sorted([doc] + self.docs,
                           key = lambda d: d._id)
        self.index[doc._id] = doc
        
    def find(self, query: Query =None) -> List[Doc]:
        """ Returns all the douments satisfying the query """
        # for now return all documents
        return self.docs
        
    def getDoc(self, id: str) -> Optional[Doc]:
        """ fetches a doc based on its _id; if it wasn't there, 
        returns None. 
        """
        if id in self.index:
            return self.index[id]
        else:
            return None
        
    def removeDoc(self, id: str) -> None:
        """ Remove the document with a particular _id """
        if id in self.index:
            self.index.pop(id, None)
            self.docs = [d for d in self.docs if d._id != id]
            
    def newId(self) -> str:
        """ return a new, unused _id for this document """        
        

#---------------------------------------------------------------------

#end
