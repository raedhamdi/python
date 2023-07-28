from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "no secret in github"
@app.route('/')
def index():
    return render_template("index.html ")

@app.route('/process', methods=['POST'])
def process ():
    print("*"*20,"PROCESS - FORM RECEIVED", "*"*20)
    print ("-" *20,  request.form , "-" *20)
    print (f"USERNAME : {request.form['username']} \n AGE : {request.form['age']} \n FAVORIE FOOD : {request.form['fav_food']} ")
    #return render_template('display.html', username = request.form['username'] , age = request.form['age'], fav_food = request.form['fav_food'])
    session['name'] = request.form['name']
    session['dojo location'] = request.form['dojo location']
    session['favorite language'] = request.form['favorite language']
    return redirect('/display')


@app.route('/display')
def display():
    print("/"*20,request.form,"/"*20)
    print( session['name'] )
    print(session['dojo location'] )
    print(session['favorite language'] )
    return render_template("display.html")
if __name__ =='__main__':
    app.run(debug= True)
