#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.yacc as yacc
import sys
import random
# Get the token map from the lexer.  This is required.
from lexer import GoLexer

class GoParser:
    tokens = GoLexer.tokens
    principal_type = None
    # No terminales en minuscula
    # Terminales en mayuscula, vienen del lexer
    #TODO: multiple newlines between definitions
    def p_initial_multiple(self, p):
        'initial : definition NEWLINE initial'
        p[0] = p[3]
        p[0][p[1]['identifier']] = p[1]['type']
        self.principal_type = p[1]['identifier']

    def p_initial_single(self, p):
        'initial : definition'
        p[0] = { p[1]['identifier'] : p[1]['type'] }
        self.principal_type = p[1]['identifier']

    def p_definition(self, p):
        'definition : TYPE ID type'
        p[0] = {
            'identifier' : p[2],
            'type' : p[3]        
        }
        #self.deps[p[2]] = p[3]['ids']

    def p_type(self, p):
        '''type : complex 
                | basic
                | ID'''
        p[0] = p[1]
   
    def p_str(self, p):
        'basic : STR' 
        p[0] = 'string'

    def p_int(self, p):
        'basic : INT' 
        p[0] = 'int'
    
    def p_float(self, p):
        'basic : FLOAT' 
        p[0] = 'float'
    def p_bool(self, p):
        'basic : BOOL' 
        p[0] = 'bool'


    def p_array(self, p):
        'basic : BRACKETS type' 
        p[0] = 'array ' + p[2]

    def p_complex(self, p):
        'complex : STRUCT LBRACE NEWLINE list RBRACE'
        p[0] = p[4]
        

    def p_list(self,p):
        'list : ID type NEWLINE list'
        p[0] = p[4]
        p[0][p[1]] = p[2]

    def p_list_end(self, p):
        'list : lambda'
        p[0] = {}


    #Define el lambda de la gramatica
    def p_lambda(self, p): 
        'lambda :'
        pass

    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error:", p, file=sys.stderr)

    # Build the parser
    def build(self,**kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
    def parse(self, data):
        return self.parser.parse(data), self.principal_type

