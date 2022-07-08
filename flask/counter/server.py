from flask import Flask, redirect, render_template, request, session
import base64

app = Flask(__name__)
app.secret_key = 'secretkey'



@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('counter.html')


@app.route('/destroy_session')
def refresh():
    session.clear()
    return redirect('/')


@app.route('/add_two')
def add_two():
    session['counter'] += 2
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)

# base64.urlsafe_b64decode('eyJ1c2VyZW1haWwiOiJ0ZXN0ZXJAZW1haWwuY29tIiwidXNlcm5hbWUiOiJCaWxseSJ9==')