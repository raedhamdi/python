from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.band import Band
from flask_app.models.user import User

@app.route('/bands/new')
def new_band():
    if not 'user_id' in session:
       return redirect ('/')
    user = User.get_by_id({'id': session['user_id']})
    return render_template("new_band.html", user = user)




@app.route('/my_bands')
def my_bands():
   if not 'user_id' in session:
      return redirect('/')
   user = User.get_by_id({'id':session['user_id']})
   bands = Band.get_user_bands({'user_id':session['user_id']})
   return render_template("my_bands.html", user = user, bands= bands)



@app.route('/bands/<int:band_id>/edit')
def edit_band(band_id):
    if 'user_id' not in session:
      return redirect('/')
    band = Band.get_by_id({'id':band_id})
    user = User.get_by_id({'id': session['user_id']})
    return render_template("edit_band.html", band = band, user=user)

@app.route('/bands/create', methods=['POST'])
def add_band():
   
    if Band.validate(request.form):
        data = {
            **request.form,
            'user_id':session['user_id'] 

        }
        Band.create(data)
        return redirect('/dashboard')
    return redirect ('/bands/new')

@app.route('/bands/<int:band_id>/update', methods=['POST'])
def update_band(band_id):
   data = {
      **request.form,
      'id': band_id
   }
   print("*******REQUEST FORM******************",data)
   Band.update(data)
   return redirect('/dashboard')

@app.route('/bands/<int:band_id>/destroy', methods = ['POST'])
def cancel(band_id):
   Band.delete({'id':band_id})
   return redirect('/dashboard')
