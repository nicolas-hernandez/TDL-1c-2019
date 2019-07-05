#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from rand import rint, rstring, rfloat, rbool, randomI

class JsonBuilder:
    def __init__(self, ast):
        self.ast = ast
        self.buildAST()

    def buildAST(self):
        for key1, value in self.ast.items():
            for key2, value2 in self.ast.items():
                if key1 != key2:
                    self.replaceAttributeIn(key1, value, key2, value2)
        print(self.ast)
    
    def replaceAttributeIn(self, key1, keyValue, key2, key2Value):
        for identifier, kind in keyValue.items():
            if kind == key2:
               keyValue[identifier] = key2Value 

