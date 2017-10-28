from collections import namedtuple

TOKENS = namedtuple('TOKENS', ('TYPE', 'LITERAL'))

ASSIGN = TOKENS('ASSIGN', '=')
ILLEGAL = TOKENS('ILLEGAL', 'ILLEGAL')
EOF = TOKENS('EOF', ':')
IDENT = TOKENS('IDENT', 'IDENT')
PLUS = TOKENS('PLUS', '+')
COMMA = TOKENS('COMMA', ',')
SEMICOLON = TOKENS('SEMICOLON', ';')
INT = TOKENS('INT', 'INT')
LPAREN = TOKENS('LPAREN', '(')
RPAREN = TOKENS('RPAREN', ')')
LBRACE = TOKENS('LBRACE', '{')
RBRACE = TOKENS('RBRACE', '}')
LESS = TOKENS('LESS', '<')
GREAT = TOKENS('GREAT', '>')
EXCLAIM = TOKENS('EXCLAIM', '!')
FSLASH = TOKENS('FSLASH', '/')
STAR = TOKENS('STAR', '*')
EQ = TOKENS('EQ', '==')
NOT_EQ = TOKENS('NOT_EQ', '!=')


keywords = {'fn': 'FUNCTION', 'let':'LET', 'if':'IF', 'else':'ELSE', 
            'return':'RETURN', 'true':'TRUE', 'false':'FALSE'}

class Tokens(object):
    def __init__(self, tokenType, literal):
        self.tokenType = tokenType
        self.literal = literal

    @staticmethod
    def lookUpIdentifier(identifier):
        return keywords.get(identifier, IDENT.TYPE)
       
        

    


