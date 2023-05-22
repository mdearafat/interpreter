# Interpreter for a Toy Language
This repository contains an interpreter for a toy language. It is developed as a simple project to understand the fundamentals of compilers and interpreters.

# Author
Md Arafat

# Project Structure
The project is divided into three main parts:
Lexer: The Lexer class reads an input string and produces a stream of tokens.
Parser: The Parser class takes a stream of tokens from a Lexer, and transforms them into an abstract syntax tree (AST).
Interpreter: The Interpreter class is responsible for walking through the AST and performing the computations.

# How to Run
Run: python main.py
Then input your program.

# Sample Inputs
Here are some sample inputs you can try:
x = 001;

x_2 = 0;

x = 0
y = x;
z = ---(x+y);

x = 1;
y = 2;
z = ---(x+y)*(x+-y);

# Language Specification
The toy language consists of simple mathematical and assignment expressions. It supports addition, subtraction, multiplication, and parentheses for defining precedence.

# Limitations
No support for division operation.
No support for floating-point numbers.
No support for strings or other data types.
