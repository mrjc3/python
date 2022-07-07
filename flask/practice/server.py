from flask import Flask, render_template

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

@app.route('/multiplication_table/<int:x>/<int:y>')
def multiplication_table(x,y):
    results = []
    
    # this is to add the headers to the multiplication table <-- its confusing
    table_header = ['x']
    for i in range(y+1):
        table_header.append(i)
    results.append(table_header)
    
    
    for i in range(x+1):
        # every new row starts with i for the header <-- thats where the [i] comes from
        new_row = [i]
        for j in range(y+1):
            new_row.append(i * j)
        results.append(new_row)

    return render_template("table.html", results=results)


if __name__ == '__main__':
    app.run(debug=True)