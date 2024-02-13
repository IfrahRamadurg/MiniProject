#!/usr/bin/python3
#testcases for scientific calculator
import unittest
from ScientificCalculatorMethods import compute_sqrt,compute_factorial,compute_log,compute_power

class TestCalculator(unittest.TestCase):

    def test_compute_sqrt(self):
        """
            Testcase to compute square root of a given number
        """
        data=4
        result=compute_sqrt(data)
        self.assertEqual(result,2)

    def test_compute_factorial(self):
        """
            Testcase to compute factorial of a given number
        """
        data=5
        result=compute_factorial(data)
        self.assertEqual(result,120)

    def test_compute_log(self):
        """
            Testcase to compute natural logarithm of a given number
        """
        data=2
        result=compute_log(data)
        self.assertEqual(result,0.69)

    def test_compute_power(self):
        """
            Testcase to compute power of a given number
        """
        base_number=7
        power_number=3
        result=compute_power(base_number,power_number)
        self.assertEqual(result,343)

if __name__=='__main__':
    unittest.main()
