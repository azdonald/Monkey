import unittest
from collections import defaultdict
from monkey.lexer import Lexer
from monkey.tokens import *


testToken = defaultdict(lambda:'IDENT')
testToken['='] = 'ASSIGN'
testToken['+'] = 'PLUS'
testToken['('] = 'LPAREN'
testToken[')'] = 'RPAREN'
testToken['{'] = 'LBRACE'
testToken['}'] = 'RBRACE'
testToken[';'] = 'SEMICOLON'
testToken[','] = 'COMMA'
testToken[''] = 'EOF'



class TestLexer(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass

    def test_nextToken(self):
        inputs = 'LET=+(){};'
        l = Lexer(inputs)   
        l.readChar()     
        for i in range(len(inputs)):        
            tk = l.nextToken()
            #print 'Literal is ' + tk.literal
            self.assertEquals(tk.tokenType, testToken[tk.literal])
            #self.assertEquals(tk.literal, l.ch)
            


if __name__ == '__main__':
    unittest.main()


