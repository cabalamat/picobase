# table.py = a Table in a Database


from typing import *

from picotypes import *
from database import Database
from doc import Doc

#---------------------------------------------------------------------

class Index:
    """ an index to a table """
    
    def __init__(self, table: 'Table')->None:
        self.table = table # type: Table
        self.data = [] # type: List[Tuple[IdType,int]]
        
    def addIndex(self, docId: IdType, docIx: int)->None:
        pass

#---------------------------------------------------------------------

class Table:
    
    def __init__(self, db: Database, name: str)->None:
        self.name = name
        self.db = db
        self.docs = [] # type: List[Doc]
        self.index = Index(self)
        self.nextId = 1 # type: int
        
    def addDoc(self, doc: Doc) -> None:
        """ Adds a document to this table. 
        gives it an _id if need be.
        """
        if doc.hasId():
            if self.getDoc(doc._id):
                self.removeDoc(doc._id)           
        else:
            doc._id = self.newId()   
                    
        self.docs.append(doc)
        self.index.addIndex(doc._id, len(self.docs)-1)
        
    def find(self, query: Query =None) -> Iterator[Doc]:
        """ Returns all the documents satisfying the query """
        # for now return all documents
        if query:            
            for doc in self.docs:
                if doc.satisfies(query):
                    yield doc
            #//for    
        else:
            # no query
            for doc in self.docs:
                yield doc
            #//for    
        
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
            
    def count(self) -> int:
        """ return the number of documents in this table """
        return len(self.docs)
            
    def newId(self) -> str:
        """ return a new, unused _id for this document """ 
        r = "%d" % self.nextId
        self.nextId += 1
        return r
        

#---------------------------------------------------------------------

#end
