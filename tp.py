#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
import sys
import json
from lexer import GoLexer
from parser import GoParser
from builder import InstanceBuilder

def parseArgs():
    parser = argparse.ArgumentParser(description='Translator, from GO to JSON.')
    parser.add_argument("--test",  help="Run a little test.", action='store_true')
    parser.add_argument("--debug",  help="Enable mode debug.", action='store_true')
    args = parser.parse_args()                                            
    return args

def testCase(lexer, parser):
    text ='''type persona struct {
    nombre  string
    edad    int
    ncapo pais
    ventas  []float64
    activo  bool
}
type pais struct {
    nombre string
    codigo struct {
        prefijo string
        sufijo  string
    }
}'''
    print(lexer.test(text))
    print(parser.test(text))

    

if __name__ == "__main__":
    args = parseArgs()
    l = GoLexer()
    l.build()        
    p = GoParser()
    p.build(debug=args.debug)
    if args.test:
        testCase(l, p)
    else:
        data = sys.stdin.read().rstrip()
        ast, principal_type = p.parse(data)
        type_instance = InstanceBuilder(ast, principal_type).randomInstance()
        print(json.dumps(type_instance, indent=4))

        
