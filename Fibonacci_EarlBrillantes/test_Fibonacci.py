#!/usr/bin/python
import unittest
from Fibonacci import Fibonacci
fibo = Fibonacci()

class testFibonacci(unittest.TestCase):

    def test_fibonacci_Input10_return(self):
        print("Executed")
        input = 10
        expected = '0,1,1,2,3,5,8,13,21,34'
        result = fibo.executeFibonacciSeries(input)
        self.assertEqual(result,expected)
    
    def test_fibonacci_Input8_return(self):
        input = 8
        expected = '0,1,1,2,3,5,8,13'
        result = fibo.executeFibonacciSeries(input)
        self.assertEqual(result,expected)
    
    def test_fibonacci_Input0_return(self):
        input = 0
        expected = '0'
        result = fibo.executeFibonacciSeries(input)
        self.assertEqual(result,expected)

if __name__=='__main__':
    unittest.main()
        