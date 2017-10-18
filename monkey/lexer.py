from .tokens import *

class Lexer:
    def __init__(self, inputs, position=0, readPosition=0, ch=0):
        self.inputs = inputs
        self.position = position
        self.readPosition = readPosition
        self.ch = ch
        self.readChar()
    
    def readChar(self):
        if self.readPosition >= len(self.inputs):
            self.ch = 0
        else:
            self.ch = self.inputs[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

       
    def nextToken(self):
        self.skipWhiteSpaces()              
        if self.ch == '=':
            if self.peek() == '=':
                literal = self.ch
                self.readChar()
                literal += self.ch
                tok = Tokens(EQ.TYPE,literal)
            else:
                tok = Tokens(ASSIGN.TYPE,self.ch)
        elif self.ch == '!':
            if self.peek() == '=':
                literal = self.ch
                self.readChar()
                literal += self.ch
                tok = Tokens(NOT_EQ.TYPE,literal)
            else:
                tok = Tokens(EXCLAIM.TYPE,self.ch)
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
        elif self.ch == '!':
            tok = Tokens(EXCLAIM.TYPE, self.ch)
        elif self.ch == '/':
            tok = Tokens(FSLASH.TYPE, self.ch)
        elif self.ch == '*':
            tok = Tokens(STAR.TYPE, self.ch)
        elif self.ch == '<':
            tok = Tokens(LESS.TYPE, self.ch)
        elif self.ch == '>':
            tok = Tokens(GREAT.TYPE, self.ch)
        elif self.ch == ' ':
            tok = Tokens(EOF.TYPE, '')
        else:
            if self.isLetter(self.ch):
                literal = self.readIdentifier()
                tkType = Tokens.lookUpIdentifier(literal)
                tok = Tokens(tkType, literal)
                return tok
            elif self.isDigit(self.ch):
                literal = self.readNumber()
                tkType = INT.TYPE
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

    def skipWhiteSpaces(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.readChar()

    def isDigit(self, ch):
        return '0' <= ch and ch <= '9'

    def readNumber(self):
        position = self.position
        while self.isDigit(self.ch):
            self.readChar()
        return self.inputs[position:self.position]

    def peek(self):
        if self.readPosition >= len(self.inputs):
            return 0
        return self.inputs[self.readPosition]
