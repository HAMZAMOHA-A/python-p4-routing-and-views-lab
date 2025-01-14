#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:message>')
def print_string(message):
    print(message)  # Print the string to the console
    return f'<h1>{message}</h1>'  # Return the string in the browser as an h1 element

@app.route('/count/<int:number>')
def count(number):
    numbers = [str(i) for i in range(number)]
    return '<br>'.join(numbers)

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div' and num2 != 0:
        result = num1 / num2
    elif operation == '%' and num2 != 0:
        result = num1 % num2
    else:
        return f"Error: Invalid operation or division by zero"
    
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5555)
