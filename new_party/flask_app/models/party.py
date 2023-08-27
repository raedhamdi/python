from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
#from datetime import datetime

class Party:    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id'] # must add to create
        self.title = data_dict['title']
        self.location = data_dict['location']
        self.all_ages = data_dict['all_ages']
        self.date = data_dict['date']
        self.description = data_dict['description']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.poster= ""
#------create
    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO parties
        (title, user_id, location, date, all_ages, description) 
        VALUES (%(title)s,%(user_id)s,%(location)s,%(date)s, %(all_ages)s, %(description)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
# ----- get all
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM parties
                   JOIN users on parties.user_id = users.id 
                   ;"""
        results = connectToMySQL(DATABASE).query_db(query)
        print("**********", results)
        all_parties = []
        for row in results:
            party=cls(row)
            party.poster = f"{row['first_name']} {row['last_name']}"
            all_parties.append(party)
        return all_parties
    @classmethod
    def get_user_parties(cls, data_dict):
        query = """SELECT * FROM parties
                   WHERE user_id = %(user_id)s
                   ;"""
        results = connectToMySQL(DATABASE).query_db(query, data_dict)
        all_parties = []
        for row in results:
            all_parties.append(cls(row))
        return all_parties
# ---- get one by id
    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM parties
                  JOIN users
                  ON parties.user_id = users.id
                  WHERE parties.id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        party = cls(result[0])
        party.poster = result[0]['first_name'] +" "+result[0]['last_name']
        return party
        
    #--- update
    @classmethod
    def update(cls, data_dict):
        query = """UPDATE parties 
                   SET
                   title = %(title)s, location= %(location)s, date= %(date)s,
                     all_ages= %(all_ages)s, description= %(description)s
                     WHERE id=%(id)s;
                   """
        return connectToMySQL(DATABASE).query_db(query, data_dict)
   
    # ---delete
    @classmethod
    def delete(cls, data_dict):
        query = """ DELETE FROM parties WHERE id =%(id)s;"""
        return connectToMySQL (DATABASE).query_db(query,data_dict)


    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['title'])<2:
            is_valid =False
            flash("Title not valid", "title")
                
        if len(data_dict['location'])<2:
            is_valid =False
            flash("Location not valid", "location")
        
        if len(data_dict["description"])<7:
            is_valid = False
            flash("Description too short", "description")

        if data_dict["date"] =="":
            is_valid = False
            flash("Date is required", "date")
       
        #elif data_dict["date"]< datetime.now():
         #   is_valid = False
        # flash ("Date must be in the future" , "date")
        return is_valid