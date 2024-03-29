#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.yacc as yacc
import sys
# Get the token map from the lexer.  This is required.
from lexer import GoLexer

class GoParser:
    tokens = GoLexer.tokens
    principal_type = None
    # No terminales en minuscula
    # Terminales en mayuscula, vienen del lexer
    def p_initial_multiple(self, p):
        'initial : definition  initial'
        p[0] = { p[1]['identifier'] : p[1]['type'] }
        if p[1]['identifier'] in p[2].keys():
            print("Syntax error: Redefined type {} found on line {}".format(p[1]['identifier'], p[1]['lineno']), file=sys.stderr)
            sys.exit(1)
        p[0].update(p[2]) 
        self.principal_type = p[1]['identifier']

    def p_initial_single(self, p):
        'initial : definition'
        p[0] = { p[1]['identifier'] : p[1]['type'] }
        self.principal_type = p[1]['identifier']

    def p_definition(self, p):
        'definition : TYPE ID type'
        p[0] = {
            'identifier' : p[2],
            'type' : p[3],
            'lineno': p.lineno(2)
        }

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
        'basic : LBRACKET RBRACKET type' 
        p[0] = {'[]': p[3]}

    def p_complex(self, p):
        'complex : STRUCT LBRACE list RBRACE'
        p[0] = p[3]
        

    def p_list(self,p):
        'list : ID type list'
        p[0] = { p[1] : p[2] }
        if p[1] in p[3].keys():
            print("Syntax error: Redefined attribute {} found on line {}".format(p[1], p.lineno(1)), file=sys.stderr)
            sys.exit(1)
        p[0].update(p[3])

    def p_list_end(self, p):
        'list : lambda'
        p[0] = {}


    #Define el lambda de la gramatica
    def p_lambda(self, p): 
        'lambda :'
        pass

    # Error rule for syntax errors
    def p_error(self, p):
        if p is None:
            print("Syntax error: unexpected end of file while parsing.", file=sys.stderr)
        else:
            print("Syntax error: Unexpected {} found on line {}".format(p.value, p.lineno), file=sys.stderr)
        sys.exit(1)

    # Build the parser
    def build(self,**kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
    def parse(self, data):
        return self.parser.parse(data), self.principal_type

