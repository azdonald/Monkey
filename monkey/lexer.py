from .tokens import *

class Lexer:
    def __init__(self, inputs, position=0, readPosition=0, ch=0):
        self.inputs = inputs
        self.position = position
        self.readPosition = readPosition
        self.ch = ch
    
    def readChar(self):
        if self.readPosition >= len(self.inputs):
            self.ch = 0
        else:
            self.ch = self.inputs[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

       
    def nextToken(self): 
              
        if self.ch == '=':
            tok = Tokens(ASSIGN.TYPE, self.ch)
        elif self.ch == ';':
            tok = Tokens(SEMICOLON.TYPE, self.ch)
        elif self.ch == '(':
            tok =Tokens(LPAREN.TYPE, self.ch)
        elif self.ch == ')':
            tok = Tokens(RPAREN.TYPE, self.ch)
        elif self.ch == ',':
            tok = Tokens(COMMA.TYPE, self.ch)
        elif self.ch == '+':
            tok = Tokens(PLUS.TYPE, self.ch)
        elif self.ch == '{':
            tok = Tokens(LBRACE.TYPE, self.ch)
        elif self.ch == '}':
            tok = Tokens(RBRACE.TYPE, self.ch)
        elif self.ch == ' ':
            tok = Tokens(EOF.TYPE, '')
        else:
            if self.isLetter(self.ch):
                literal = self.readIdentifier()
                tkType = Tokens.lookUpIdentifier(literal)
                tok = Tokens(tkType, literal)
                return tok
            else:
                tok = Tokens(ILLEGAL.TYPE, self.ch)
        
        self.readChar()
        return tok

    def isLetter(self, ch):
        return 'a' <= ch and ch <= 'z' or 'A' <= ch and ch <= 'Z' or ch == '_'

    def readIdentifier(self):
        position = self.position
        while self.isLetter(self.ch):
            self.readChar()
        return self.inputs[position:self.position]

