#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from rand import randomValue
from copy import deepcopy

class InstanceBuilder:

    def __init__(self, ast, principal):
        self.ast = ast
        self.principal = principal
        self.buildAST()

    def randomInstance(self):
        instance = randomValue(self.ast[self.principal])
        return instance

    def buildAST(self):
        for key1, value in self.ast.items():
            for key2, value2 in self.ast.items():
                if key1 != key2:
                    self.replaceAttributeIn(value, key2, value2)
    
    def replaceAttributeIn(self, value, key2, key2Value):
        for identifier, kind in value.items():
            if kind == key2:
                value[identifier] = deepcopy(key2Value)
            elif type(kind) is dict:
                self.replaceAttributeIn(kind, key2, key2Value)
                    


