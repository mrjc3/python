
import re
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/play')
def index():
    return render_template("index.html", times=3)

@app.route('/play/<int:num>')
def level2(num):
    return render_template("index.html", times=int(num))

@app.route('/play/<int:num>/<string:color>')
def level3(num, color):
    return render_template("index.html", times=num, color=color)





if __name__ == '__main__':
    app.run(debug=True)