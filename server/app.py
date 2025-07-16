#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# INDEX ROUTE
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# PRINT STRING ROUTE
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

# COUNT ROUTE
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "\n".join(str(i) for i in range(parameter)) + "\n"
    return numbers



# MATH ROUTE
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is not allowed", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result)
