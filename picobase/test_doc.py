# test_doc.py = test doc.py

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

    def test_satisfies(self):
        d = Doc(aaa=3, bbb=6, c='cat')
        r = d.satisfies(None)
        self.assertTrue(r, "query None -> always True") 
        r = d.satisfies({})
        self.assertTrue(r, "query {} -> always True") 
        
        r = d.satisfies({'aaa':3})
        self.assertTrue(r, "{'aaa':3} -> True") 
        r = d.satisfies({'aaa':66})
        self.assertFalse(r, "{'aaa':66} -> False") 
        
        r = d.satisfies({'c':'cat'})
        self.assertTrue(r, "{'c':'cat'} -> True") 
        r = d.satisfies({'c':'owl'})
        self.assertFalse(r, "{'c':'owl'} -> False") 
        
        # multiple test must all be right
        r = d.satisfies({'aaa':3, 'bbb':6, 'c':'cat'})
        self.assertTrue(r, "{'aaa':3, 'bbb':6, 'c':'cat'} -> True") 
        r = d.satisfies({'aaa':3, 'bbb':6, 'c':'llama'})
        self.assertFalse(r, "{'aaa':3, 'bbb':6, 'c':'llama'} -> False") 
        
        # tests to non-existent field fail
        r = d.satisfies({'aaa':3, 'bbb':6, 'cc':'cat'})
        self.assertFalse(r, "{'aaa':3, 'bbb':6, 'cc':'cat'} -> False") 
        r = d.satisfies({'no':'nnn'})
        self.assertFalse(r, "{'no':'nnn'} -> False") 
        

#---------------------------------------------------------------------
    
group = lintest.TestGroup()
group.add(T_Doc)

if __name__=='__main__': group.run()



#end
