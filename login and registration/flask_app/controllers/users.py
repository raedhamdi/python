from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt =Bcrypt(app)

#----index page
@app.route('/')
def index():
    return render_template("index.html")

#----dashboard
@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", user =logged_user)

# ----register

@app.route('/users/create',methods=['POST'])
def register():
    # get the form data from the front-end

    print(request.form)
    # validate the form data
    # if data is valid

    if User.validate(request.form):
        #secure password = hash the password using bcrypt
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
            'password':pw_hash
        }
         # create the new user
        user_id = User.create(data)
        session['user_id'] = user_id
        return redirect ('/dashboard')
    # if data not valid
    return redirect ('/')
    
   #-------login

@app.route('/login', methods=['POST'])
def login():  
    #get user by email
    user = User.get_by_email({'email':request.form['email']})
    # if user not exist : redirect to index and display errors
    if not user:
        flash("Invalid Email/Password", "login")
        return redirect('/')
    # if user exist : check password
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

#-----logout
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')
    