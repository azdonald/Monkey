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
testToken['let'] = 'LET'
testToken['5'] = 'INT'
testToken['10'] = 'INT'
testToken['9'] = 'INT'
testToken['fn'] = 'FUNCTION'
testToken['if'] = 'IF'
testToken['else'] = 'ELSE'
testToken['return'] = 'RETURN'
testToken['<'] = 'LESS'
testToken['>'] = 'GREAT'
testToken['!'] = 'EXCLAIM'
testToken['/'] = 'FSLASH'
testToken['*'] = 'STAR'
testToken['=='] = 'EQ'
testToken['!='] = 'NOT_EQ'
testToken['-'] = 'ILLEGAL'



class TestLexer(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass

    def test_nextToken(self):
        inputs = '''let five = 5;
                    let ten = 10;
                    let add = fn(x, y) {
                    x + y;
                    };
                    let result = add(five, ten);
                    !-/*5;
                    5 < 10 > 5;
                    10 == 10;
                    10 != 9;'''
        l = Lexer(inputs)
        while l.readPosition <= len(inputs):
            tk = l.nextToken()
            print 'Literal is ' + tk.literal
            self.assertEquals(tk.tokenType, testToken[tk.literal])     
        
            


if __name__ == '__main__':
    unittest.main()


