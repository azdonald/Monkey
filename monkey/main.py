from .tokens import *
from .lexer import Lexer

print '>>> Welcome to the Monkey programming language'

s = raw_input('>>  ')
while s != 'END':
    tok = Lexer(s)
    while tok.readPosition <= len(s):
        tk = tok.nextToken()
        print 'Token type  is {} while literal is {} '.format(tk.tokenType, tk.literal)     
    s = raw_input('>>  ')