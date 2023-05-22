# The Interpreter class is responsible for walking through the AST and performing the computations.
class Interpreter:
    def __init__(self, parser):
        self.parser = parser
        # Variables dictionary to store variable values
        self.variables = {}

    def error(self, message):
        raise Exception(message)

    # The visit method is a dispatcher that calls the appropriate method for the given node type.
    def visit(self, node):
        method_name = 'visit_' + node[0]
        visitor = getattr(self, method_name, self.error)
        return visitor(node)

    # The methods below each handle a specific node type.

    def visit_assignment(self, node):
        _, name, value_node = node
        value = self.visit(value_node)
        self.variables[name] = value
        return value

    def visit_binop(self, node):
        _, left_node, op, right_node = node
        left = self.visit(left_node)
        right = self.visit(right_node)
        if op == 'PLUS':
            return left + right
        elif op == 'MINUS':
            return left - right
        elif op == 'MUL':
            return left * right

    def visit_unaryop(self, node):
        _, op, operand_node = node
        operand = self.visit(operand_node)
        if op == '+':
            return operand
        elif op == '-':
            return -operand

    def visit_integer(self, node):
        _, value = node
        return value

    def visit_identifier(self, node):
        _, name = node
        if name not in self.variables:
            self.error("Uninitialized variable '{}'".format(name))
        return self.variables[name]

    # The interpret method is the main entry point into the Interpreter. It parses the input and then walks the AST.
    def interpret(self):
        tree = self.parser.parse()
        for node in tree:
            self.visit(node)
        return self.variables
