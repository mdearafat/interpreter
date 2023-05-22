import re

# The Token class represents a token produced by the lexer. Each token has a type (like 'INTEGER', 'PLUS', or 'IDENTIFIER')
# and a value (the actual text that was read from the input).
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

# The Lexer class reads an input string and produces a stream of tokens. The input string is a program written in your toy language.
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    # If the lexer encounters an invalid character, it raises an exception.
    def error(self):
        raise Exception('Invalid character')

    # The get_next_token method reads characters from the input string until it forms a complete token, then returns that token.
    # If it encounters whitespace, it simply skips over it. If it encounters a character that doesn't make sense, it calls the error method.
    def get_next_token(self):
        while self.pos < len(self.text):
            if self.text[self.pos].isspace():
                self.pos += 1
                continue
            if self.text[self.pos].isdigit():
                return self.number()
            if self.text[self.pos] == '+':
                self.pos += 1
                return Token('PLUS', '+')
            if self.text[self.pos] == '-':
                self.pos += 1
                return Token('MINUS', '-')
            if self.text[self.pos] == '*':
                self.pos += 1
                return Token('MUL', '*')
            if self.text[self.pos] == '/':
                self.pos += 1
                return Token('DIV', '/')
            if self.text[self.pos] == '(':
                self.pos += 1
                return Token('LPAREN', '(')
            if self.text[self.pos] == ')':
                self.pos += 1
                return Token('RPAREN', ')')
            if self.text[self.pos] == ';':
                self.pos += 1
                return Token('SEMI', ';')
            if self.text[self.pos] == '=':
                self.pos += 1
                return Token('EQUAL', '=')
            if re.match('[a-zA-Z_][a-zA-Z0-9_]*', self.text[self.pos:]):
                return self.identifier()
            self.error()
        return Token('EOF', None)

    # The number method reads characters until it forms a complete integer, then returns a token representing that integer.
    def number(self):
        result = ''
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            result += self.text[self.pos]
            self.pos += 1
        if len(result) > 1 and result.startswith('00'):
            self.error()
        return Token('INTEGER', int(result))

    # The identifier method reads characters until it forms a complete identifier (a variable name, in this language), then returns a token representing that identifier.
    def identifier(self):
        result = ''
        while self.pos < len(self.text) and (self.text[self.pos].isalnum() or self.text[self.pos] == '_'):
            result += self.text[self.pos]
            self.pos += 1
        return Token('IDENTIFIER', result)
