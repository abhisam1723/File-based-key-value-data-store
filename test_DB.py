import unittest
from DB import Create
class TestCreate(unittest.TestCase):
    
    def test_set(self):
        k = Create()
        self.assertEqual(k.set('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','too long key'),'Length of key beyond limit : Shouldnot be more than 32CHARS')
        self.assertEqual(k.set('in limit','will return None'),None)

    def test_read(self):
        k = Create('','',3)
        k.set('fresh','works')
        self.assertEqual(k.read('fresh'),'works')
        self.assertEqual(k.read('mind'),'Key error')

    def test_delete(self):
        k = Create('','',3)
        k.set('fresh','works')
        k.set('mind','tree')
        self.assertEqual(k.delete('mind'),True)
        self.assertEqual(k.delete('mind'),'No such key to delete')

    

if __name__ == '__main__':
    unittest.main()