#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.yacc as yacc
import sys

# Get the token map from the lexer.  This is required.
from lexer import GoLexer
from rand import rint, rstring, rfloat, rbool

class GoParser:
    tokens = GoLexer.tokens
    # No terminales en minuscula
    # Terminales en mayuscula, vienen del lexer
    #TODO: multiple newlines between definitions
    def p_initial_multiple(self, p):
        'initial : definition NEWLINE initial'
        p[0] = p[1] + p[3]

    def p_initial_single(self, p):
        'initial : definition'
        p[0] = p[1]

    def p_definition(self, p):
        'definition : TYPE ID type'
        p[0] = p[3]

    def p_type(self, p):
        '''type : complex 
                | basic
                | ID'''
        p[0] = p[1]
   
    # TODO: testear como lexea/parsea los brackets, con espacio y sin espacio
    # creo que al ignorar espacios puedo aceptar "[]  int". Es valido?
    def p_str(self, p):
        'basic : STR' 
        p[0] = rstring()

    def p_int(self, p):
        'basic : INT' 
        p[0] = str(rint())
    
    def p_float(self, p):
        'basic : FLOAT' 
        p[0] = str(rfloat())
    def p_bool(self, p):
        'basic : BOOL' 
        p[0] = str(rbool())
    def p_array(self, p):
        'basic : BRACKETS type' 
        p[0] = "["+ p[2] +"]"

    def p_complex(self, p):
        'complex : STRUCT LBRACE NEWLINE list RBRACE'
        p[0] = "{ \n" + p[4] + "}"

    def p_list(self,p):
        'list : ID type NEWLINE list'
        p[0] = '"' + p[1] + '": '+ p[2] + ",\n" + p[4]
    def p_list_end(self, p):
        'list : lambda'
        p[0] = ''


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
    def test(self, data):
        return self.parser.parse(data)

