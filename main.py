from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def main():
    while True:
        try:
            # The prompt for user input, end of file is Ctrl+D
            text = input('toy language > ')
        except EOFError:
            break
        if not text:
            continue

        # Initialize the lexer with the input text
        lexer = Lexer(text)
        # Initialize the parser with the lexer
        parser = Parser(lexer)
        # Initialize the interpreter with the parser
        interpreter = Interpreter(parser)

        try:
            # Interpret the input text
            variables = interpreter.interpret()
            # Print the resulting variables and their values
            for name, value in variables.items():
                print(f'{name} = {value}')
        except Exception as e:
            # If there's an error, print it
            print(e)


if __name__ == '__main__':
    main()
