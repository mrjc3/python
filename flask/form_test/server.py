import re
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "thisisthesecretkey"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # this stores the requested info into a session. which saves info about the user that can be used on different routes - i think its the same as cookies
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    
    return redirect('/show')

@app.route('/show')
def show_user():
    print("Showing the User from the Form")
    print(request.form)
    return render_template('show.html',
                            name_on_template = session['username'],
                            email_on_template = session['useremail'],
                        )

if __name__ == '__main__':
    app.run(debug=True)