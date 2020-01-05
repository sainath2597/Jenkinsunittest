import unittest
from Cal import Calculator
class testCal(unittest.TestCase):
    def test_oper(self):
        ca=Calculator(2,3)
        self.assertEqual(ca.add(),5, msg='Add 2 numbers')
        self.assertEqual(ca.sub(),1, msg='Sub 2 numbers')
        self.assertEqual(ca.mul(),6)

if __name__ == '__main__':
    unittest.main()