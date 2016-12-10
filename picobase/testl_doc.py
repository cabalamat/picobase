# testl_doc.py = test doc.py

import lintest

from doc import Doc

#---------------------------------------------------------------------

class T_Doc(lintest.TestCase):

    def test_creation(self):
        d = Doc(aaa=3, bbb=6)
        
        self.assertTrue(d.hasattr('aaa'), "has aaa")
        self.assertFalse(d.hasattr('zxe'), "doesn't have zxe")
        self.assertEqual(d.aaa, 3, "aaa is 3")
        self.assertEqual(d.bbb, 6, "bbb is 6")

#---------------------------------------------------------------------
    
group = lintest.TestGroup()
group.add(T_Doc)

if __name__=='__main__': group.run()



#end