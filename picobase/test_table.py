# test_table.py = test <table.py>


import lintest

from doc import Doc
from table import Table
from database import Database

#---------------------------------------------------------------------

class T_Table(lintest.TestCase):

    def test_creation(self):
        db = Database("mydatabase")
        t = Table(db, "mytable")
        self.assertEqual(t.count(), 0, "no documents yet")
        
        d = Doc(foo=2, bar=3)
        t.addDoc(d)
        self.assertEqual(t.count(), 1, "1 document now")

#---------------------------------------------------------------------
 
group = lintest.TestGroup()
group.add(T_Table)

if __name__=='__main__': group.run()







#end
