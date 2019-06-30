#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import GoLexer
from rand import rint, rstring, rfloat

class GoParser:
    tokens = GoLexer.tokens
    # No terminales en minuscula
    # Terminales en mayuscula, vienen del lexer
    #TODO: multiple newlines between definitions
    def p_initial_multiple(self, p):
        'initial : definition NEWLINE initial'

    def p_initial_single(self, p):
        'initial : definition'

    def p_definition(self, p):
        'definition : TYPE ID type'
        print("parsing type: ", p[2])

    def p_type(self, p):
        '''type : complex 
                | basic
                | ID'''
   
    # TODO: testear como lexea/parsea los brackets, con espacio y sin espacio
    # creo que al ignorar espacios puedo aceptar "[]  int". Es valido?
    def p_basic(self, p):
        '''basic : STR 
                 | INT 
                 | FLOAT 
                 | BOOL 
                 | BRACKETS type'''
    
    def p_complex(self, p):
        'complex : STRUCT LBRACE NEWLINE list RBRACE'

    def p_list(self,p):
        '''list : ID type NEWLINE list 
                | lambda'''


    #Define el lambda de la gramatica
    def p_lambda(self, p): 
        'lambda :'
        print("lambda")
        pass

    # Error rule for syntax errors
    def p_error(self, p):
        
        print("Syntax error:", p)

    # Build the parser
    def build(self,**kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
    def test(self, data):
        return self.parser.parse(data)

