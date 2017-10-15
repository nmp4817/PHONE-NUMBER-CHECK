from phone_check import APIChecker
import unittest
 
class TestUM(unittest.TestCase):
 
    def test1(self):
    	i = '6823567998'
    	j = '+16823567998'
    	k = APIChecker(i)
        self.assertEqual(k,j)
        print '\nInput:',i
        print 'Expected Ouput:',j
        print 'Program Output:',k

    def test2(self):
    	i = '02143567883'
    	j = '+12143567883'
    	k = APIChecker(i)
        self.assertEqual(k,j)
        print '\nInput:',i
        print 'Expected Ouput:',j
        print 'Program Output:',k

    def test3(self):
    	i = '(682) 356 7998'
    	j = '+16823567998'
    	k = APIChecker(i)
        self.assertEqual(k,j)
        print '\nInput:',i
        print 'Expected Ouput:',j
        print 'Program Output:',k
 
    def test4(self):
    	i = '682-356-7998'
    	j = '+16823567998'
    	k = APIChecker(i)
        self.assertEqual(k,j)
        print '\nInput:',i
        print 'Expected Ouput:',j
        print 'Program Output:',k

    def test5(self):
    	i = '006823567998'
    	j = None
    	k = APIChecker(i)
        self.assertEqual(k,j)
        print '\nInput:',i
        print 'Expected Ouput:',j
        print 'Program Output:',k

    def test6(self):
    	i = '02abc143567883'
    	j = None
    	k = APIChecker(i)
        self.assertEqual(k,j)
        print '\nInput:',i
        print 'Expected Ouput:',j
        print 'Program Output:',k

    def test7(self):
    	i = '+4400ahd516328322333'
    	j = None
    	k = APIChecker(i)
        self.assertEqual(k,j)
        print '\nInput:',i
        print 'Expected Ouput:',j
        print 'Program Output:',k
 
    def test8(self):
    	i = '+102345678910'
    	j = None
    	k = APIChecker(i)
        self.assertEqual(k,j)
        print '\nInput:',i
        print 'Expected Ouput:',j
        print 'Program Output:',k


if __name__ == '__main__':
    unittest.main()