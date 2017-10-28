from .tokens import *

class Program(object):
    def __init__(self):
        self.statements = []

    def tokenLiteral(self):
        if len(self.statements) > 0:
            return self.statements[0]
        return ''


class Letstatement(object):
    def __init__(self, token, name=None, value=None):
        self.token = token
        self.name = name
        self.value = value

    def tokenLiteral(self):
        return self.token.literal

class Identifier(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def tokenLiteral(self):
        return self.token.literal


class Parser(object):
    def __init__(self, lexer, curToken, peekToken):
        self.lexer = lexer
        self.curToken = curToken
        self.peekToken = peekToken

    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.nextToken()

    def parseProgram(self):
        program = Program()
        while self.curToken.tokenType != EOF.TYPE:
            stmt = self.parseStatement()
            if stmt is not None:
                program.statements.append(stmt)
            self.nextToken()
        return program

    def parseStatement(self):
        if self.curToken.tokenType == Tokens.lookUpIdentifier('let'):
            return self.parseLetStatement()
        return None
                

    def parseLetStatement(self):
        stmt = Letstatement(self.curToken)
        if not self.expectPeek(IDENT.TYPE):
            return None
        stmt.name = Identifier(self.curToken, self.curToken.literal)
        if not self.expectPeek(ASSIGN.TYPE):
            return None
        while not self.curTokenIs(SEMICOLON.TYPE):
            self.nextToken()

        return stmt

    def curTokenIs(self, tokenType):
        print 'Current IS ' + self.peekToken.tokenType
        return self.curToken.tokenType == tokenType

    def peekTokenIs(self, tokenType):
        print 'PEEK IS ' + self.peekToken.tokenType
        return self.peekToken.tokenType == tokenType

    def expectPeek(self, tokenType):
        if self.peekTokenIs(tokenType):
            self.nextToken()
            return True
        return False
