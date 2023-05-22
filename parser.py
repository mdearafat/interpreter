from lexer import Lexer, Token
# The Parser class takes a stream of tokens from a Lexer, and transforms them into an abstract syntax tree (AST).
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    # This method ensures that the current token has the correct type. If it does, it 'consumes' the token and gets the next one from the lexer.
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    # The methods below each represent one rule of the language's grammar.
    # Each method eats tokens and calls other methods as needed to build the AST, which is returned as a nested structure of lists.

    # An assignment is an identifier followed by an equals sign and an expression, then a semicolon.
    def assignment(self):
        name = self.current_token.value
        self.eat('IDENTIFIER')
        self.eat('EQUAL')
        value = self.expr()
        self.eat('SEMI')
        return ('assignment', name, value)

    # An expression can be a term, or an expression followed by a plus or minus and a term.
    def expr(self):
        node = self.term()
        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            else:
                self.eat('MINUS')
            node = ('binop', node, token.type, self.term())
        return node

    # A term can be a factor, or a term followed by a multiplication sign and a factor.
    def term(self):
        node = self.factor()
        while self.current_token.type == 'MUL':
            self.eat('MUL')
            node = ('binop', node, 'MUL', self.factor())
        return node

    # A factor can be a number, or a plus or minus followed by a factor, or an expression in parentheses.
    def factor(self):
        token = self.current_token
        if token.type == 'PLUS':
            self.eat('PLUS')
            node = ('unaryop', '+', self.factor())
            return node
        elif token.type == 'MINUS':
            self.eat('MINUS')
            node = ('unaryop', '-', self.factor())
            return node
        elif token.type == 'INTEGER':
            self.eat('INTEGER')
            return ('integer', token.value)
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        else:
            self.eat('IDENTIFIER')
            return ('identifier', token.value)

    # The parse method parses the entire input by repeatedly calling the method for assignments.
    def parse(self):
        result = []
        while self.current_token.type != 'EOF':
            result.append(self.assignment())
        return result
