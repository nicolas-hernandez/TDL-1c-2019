#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.lex as lex
 
class GoLexer(object):
    # List of token names.   This is always required
    tokens = (
       'LBRACE',
       'RBRACE',
       'BRACKETS',
       'ID',
       'NEWLINE',
       'RPAREN',
    ) + list(reserved.values())

    reserved = {
        'string':'STR'
        'int':'INT'
        'float64':'FLOAT'
        'bool':'BOOL'
        'struct':'STRUCT'
        'type':'TYPE'
    }
    # Regular expression rules for simple tokens
    t_LBRACE   = r'\{'
    t_RBRACE   = r'\}'
    t_BRACKETS  = r'[]'

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class

    def t_ID(self, t):
        r'[A-Za-z]*'
        t.type = reserved.get(t.value,'ID') # Check for reserved words
        return t
    # Define a rule so we can track line numbers
    def t_NEWLINE(self,t):
        r'\n'
        t.lexer.lineno += 1
        return t

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    # Test it output
    def test(self,data):
        tokens = []
        self.lexer.input(data)
        for tok in self.lexer:
            tokens.append(tok)
        return tokens
 

