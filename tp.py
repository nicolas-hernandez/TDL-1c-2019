#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
import sys
from lexer import GoLexer
from parser import GoParser

def parseArgs():
    parser = argparse.ArgumentParser(description='Translator, from GO to JSON.')
    parser.add_argument("--test",  help="Run a little test. Should be deleted and replaced with unit tests instead.", action='store_true')
    parser.add_argument("--debug",  help="Enable mode debug.", action='store_true')
    args = parser.parse_args()                                            
    return args

def testCase(lexer, parser):
    text ='''type persona struct {
    nombre  string
    edad    int
    nacionalidad pais
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
        print(l.test(data))
        print(p.test(data))
