from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.party import Party
from flask_app.models.user import User
@app.route('/parties/new')
def new_party():
    if not 'user_id' in session:
       return redirect ('/')
    return render_template("new_party.html")

@app.route('/parties/<int:party_id>')
def show_one(party_id):
   if not 'user_id' in session:
      return redirect('/')
   party = Party.get_by_id({'id':party_id})
   return render_template("one_party.html", party=party)


@app.route('/my_parties')
def my_parties():
   if not 'user_id' in session:
      return redirect('/')
   user = User.get_by_id({'id':session['user_id']})
   parties = Party.get_user_parties({'user_id':session['user_id']})
   return render_template("my_parties.html", user = user, parties= parties)



@app.route('/parties/<int:party_id>/edit')
def edit_party(party_id):
    if 'user_id' not in session:
     return redirect('/')
    party = Party.get_by_id({'id':party_id})
    return render_template("edit_party.html", party = party)

@app.route('/parties/create', methods=['POST'])
def add_party():
    print("*"*10,request.form)
    if Party.validate(request.form):
        data = {
            **request.form,
            'user_id':session['user_id'] 

        }
        Party.create(data)
        return redirect('/dashboard')
    return redirect ('/parties/new')

@app.route('/parties/<int:party_id>/update', methods=['POST'])
def update_party(party_id):
   data = {
      ** request.form,
      'id':party_id
   }
   Party.update(data)
   return redirect('/dashboard')

@app.route('/parties/<int:party_id>/destroy', methods = ['POST'])
def cancel(party_id):
   Party.delete({'id':party_id})
   return redirect('/dashboard')
