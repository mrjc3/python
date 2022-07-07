import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", row=4, col=4)

@app.route('/4')
def four():
    return render_template("index.html", row=4, col=2)

@app.route('/<int:row>/<int:col>')
def input(row, col):
    return render_template("index.html", row=row, col=col)







if __name__ == '__main__':
    app.run(debug=True)