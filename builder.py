#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from rand import randomValue
from copy import deepcopy

class InstanceBuilder:

    def __init__(self, ast, principal):
        self.ast = ast
        self.deps = {}
        for maintype in ast.keys():
            self.deps[maintype] = []
        self.current = None
        self.principal = principal
        self.buildAST()

    def randomInstance(self):
        instance = randomValue(self.ast[self.principal])
        return instance

    def buildAST(self):
        for key1, value in self.ast.items():
            self.current = key1
            for key2, value2 in self.ast.items():
                if key1 != key2:
                    self.replaceAttributeIn(value, key2, value2)
        print(self.deps)
    
    def replaceAttributeIn(self, value, key2, key2Value):
        for identifier, kind in value.items():
            if kind == key2:
                self.deps[self.current] = key2
                value[identifier] = deepcopy(key2Value)
            elif type(kind) is dict:
                self.replaceAttributeIn(kind, key2, key2Value)
                    


