# database.py = a Database

from typing import *

#from table import Table

#---------------------------------------------------------------------

class Database:
    
    def __init__(self, name:str, dirPan:str = "")->None:
        """
        :param name: the name of the database
        :param dirPan: the directory it goes in. This defaults
           to ~/.picobase/{name}/
        """
        self.name = name
        self.tables = {} # type: Dict[str, Table]
        
    def __getitem__(self, tableName: str) -> 'Table':
        """ get a table, creating it if necessary """
        from table import Table
        if tableName not in self.tables:
            self.tables[tableName] = Table(self, tableName)
        return self.tables[tableName]
            

#---------------------------------------------------------------------

#end
