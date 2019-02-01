'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-01-31 22:48:01
'''
# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(201,100,150),"InvalidInput")
    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(2,3,0),"InvalidInput")
    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle(2,3,"e"),"InvalidInput")
    def testInvalidInput4(self):
        self.assertEqual(classifyTriangle("e",3,4),"InvalidInput")
    def testInvalidInput5(self):
        self.assertEqual(classifyTriangle(2.1,3,4),"InvalidInput")
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be Scalene')
    
    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 should be Isoceles')

    def testNotATriangles(self): 
        self.assertEqual(classifyTriangle(2,3,1),'NotATriangle','2,3,1 should be Not A Triangle')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

