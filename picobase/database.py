# database.py = a Database

from typing import *

#---------------------------------------------------------------------

class Database:
    
    def __init__(self, name:str, dirPan:str = "")->None:
        """
        :param name: the name of the database
        :param dirPan: the directory it goes in. This defaults
           to ~/.picobase/{name}/
        """
        self.name = name

#---------------------------------------------------------------------

#end
