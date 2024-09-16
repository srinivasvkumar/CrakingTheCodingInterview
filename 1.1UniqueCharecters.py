import unittest


def uniqueIdentifier(str):
    char_set=[False for _ in range(128)]
    
    for chr in str:
        val=ord(chr)
        if char_set[val]:
            return False
        else :
            char_set[val]=True
    return True



class Test(unittest.TestCase):
    dataT=[('abcdef'),('abcd'),('cat'),('')]
    dataF=[('srinivas'),('mama')]
    
    str="mama"
    print ("result is",uniqueIdentifier(str))     

    def test_unique(self):
        for test_string in self.dataT:
            actual=uniqueIdentifier(test_string)
            self.assertTrue(actual)
            
        for test_string in self.dataF:
            actual=uniqueIdentifier(test_string)
            self.assertFalse(actual)    

if __name__=="__main__": 
    unittest.main()           