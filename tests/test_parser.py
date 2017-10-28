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
        tk = lex.nextToken()
        pas = Parser(lex, tk, tk)
        print tk.tokenType
        program = pas.parseProgram()

        self.assertNotEqual(program, None)
        self.assertEquals(3, len(program.statements))
        print len(program)


if __name__ == '__main__':
    unittest.main()