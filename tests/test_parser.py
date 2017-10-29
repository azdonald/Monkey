import unittest
from collections import defaultdict
from monkey.lexer import Lexer
from monkey.tokens import *
from monkey.parser import *


class TestParser(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def testLetStatement(self):
        inputs = '''let five = 5;
                    let ten = 10;
                    let foobar = 838383;    :'''
        lex = Lexer(inputs)
        curtoken = lex.nextToken()
        peektoken = lex.nextToken()
        pas = Parser(lex, curtoken, peektoken)
        program = pas.parseProgram()

        self.assertNotEqual(program, None)
        self.assertEquals(3, len(program.statements))
        for i in range(len(program.statements) - 1):
            self.assertEquals(program.statements[i].tokenLiteral(), 'let')

    def testErrors(self):
        inputs = '''let five  5;
                    let ten  10;
                    let foobar  838383;    :'''
        lex = Lexer(inputs)
        curtoken = lex.nextToken()
        peektoken = lex.nextToken()
        pas = Parser(lex, curtoken, peektoken)
        program = pas.parseProgram()

        self.assertEquals(3, len(pas.errors))
        print 'Number of error is {}'.format(len(pas.errors))
        
        


if __name__ == '__main__':
    unittest.main()