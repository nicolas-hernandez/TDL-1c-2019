#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
from lexer import GoLexer
from parser import GoParser
def parseArgs():
    parser = argparse.ArgumentParser(description='Translator, from GO to JSON.')
    #parser.add_argument("", help="")            
    args = parser.parse_args()                                            

if __name__ == "__main__":
    args = parseArgs()
    # Build the lexer and try it out
    l = GoLexer()
    l.build()           # Build the lexer
    print(l.test("3 + 4"))     # Test it


    p = GoParser()
    p.build()
    print(p.test("3 + 4"))

