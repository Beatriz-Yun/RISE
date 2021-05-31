from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/calculator/<string:operation>/<int:value1>/<int:value2>')
def calculator(operation, value1, value2):
    ret = 0
    if operation == "add":
        ret = value1 + value2
    elif operation == "sub":
        ret = value1 - value2
    elif operation == "mul":
        ret = value1 * value2
    elif operation == "div":
        ret = value1 / value2

    return f'Operation {operation} with {value1} and {value2} is {ret}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

