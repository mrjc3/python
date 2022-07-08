from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    
    strawberry_data = int(request.form['strawberry'])
    raspberry_data = int(request.form['raspberry'])
    apple_data = int(request.form['apple'])
    
    
    print(request.form)
    print(f"Charging {request.form['first_name']} for {strawberry_data+raspberry_data+apple_data}")
    
    
    return render_template("checkout.html",
                            strawberry_data = strawberry_data,
                            raspberry_data = raspberry_data,
                            apple_data = apple_data,
                            first_name = request.form['first_name'],
                            last_name = request.form['last_name'],
                            student_id = request.form['student_id'],
                        )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    