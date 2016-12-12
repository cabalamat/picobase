# test_table.py = test <table.py>


import lintest

from doc import Doc
from table import Table
from database import Database

#---------------------------------------------------------------------

class T_Table(lintest.TestCase):

    def test_creation(self):
        self.db = Database("mydatabase")
        t = self.db["mytable"]
        self.assertEqual(t.count(), 0, "no documents yet")
        
        d = Doc(foo=2, bar=3)
        t.addDoc(d)
        self.assertEqual(t.count(), 1, "1 document now")
        print(d)
        
    def test_addSomeDocs(self):
        t = self.db["mytable"]
        self.assertEqual(t.count(), 1, "still 1 document")
        
        countSB = 1
        for foo in [5,4,6]:
            for bar in ['Cedric', 'Alice', 'Bob']:
                d = Doc(foo=foo, bar=bar)
                t.addDoc(d)
                countSB += 1
                self.assertEqual(t.count(), countSB, 
                    "count of documents in mytable")
            #//for
        #//for
        
    def test_find_all(self):
        """ find all the documents """
        t = self.db["mytable"]
        ds = list(t.find())
        self.assertSame(len(ds), 10, "returned all 10 douments")
        
    def test_find_q(self):
        """ find() using a query """
        t = self.db["mytable"]
        ds = list(t.find({'bar':'Alice'}))
        self.assertSame(len(ds), 3, "returned 3 douments")
        fooValues = sorted(d.foo for d in ds)
        self.assertSame(fooValues, [4, 5, 6])
        
        
        

#---------------------------------------------------------------------
 
group = lintest.TestGroup()
group.add(T_Table)

if __name__=='__main__': group.run()

#end
