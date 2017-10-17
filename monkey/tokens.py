from collections import namedtuple

TOKENS = namedtuple('TOKENS', ('TYPE', 'LITERAL'))

ASSIGN = TOKENS('ASSIGN', '=')
ILLEGAL = TOKENS('ILLEGAL', 'ILLEGAL')
EOF = TOKENS('EOF', '')
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
HYPHEN = TOKENS('HYPHEN', '-')
FSLASH = TOKENS('FSLASH', '/')
STAR = TOKENS('STAR', '*')


keywords = {'fn': 'FUNCTION', 'let':'LET', 'if':'IF', 'else':'ELSE', 'return':'RETURN'}

class Tokens:
    def __init__(self, tokenType, literal):
        self.tokenType = tokenType
        self.literal = literal

    @staticmethod
    def lookUpIdentifier(identifier):
        return keywords.get(identifier, IDENT.TYPE)
       
        

    


