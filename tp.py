#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
from lexer import GoLexer
import parser
def parseArgs():
    parser = argparse.ArgumentParser(description='Translator, from GO to JSON.')
    #parser.add_argument("", help="")            
    args = parser.parse_args()                                            

if __name__ == "__main__":
    args = parseArgs()
    # Build the lexer and try it out
    m = GoLexer()
    m.build()           # Build the lexer
    m.test("3 + 4")     # Test it
