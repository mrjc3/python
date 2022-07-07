from re import A
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hiya JOHN!!'

@app.route('/page2')
def page2():
    return "Big Daddy Kane!!"

# the term in the brackets must be the same as the parameter
@app.route('/sample/<string>')
def third_route(string):
    return f"The route contains {string}"

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x,y):
    result = x * y
    return f"the result of {x} * {y} = {result}"


if __name__ == '__main__':
    app.run(debug=True) 