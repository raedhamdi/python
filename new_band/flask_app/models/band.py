from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
#from datetime import datetime

class Band:    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id'] # must add to create
        self.band_name = data_dict['band_name']
        self.music_genre = data_dict['music_genre']
        self.home_city = data_dict['home_city']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.poster= ""
        
#------create
    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO bands
        (band_name, user_id, music_genre, home_city) 
        VALUES (%(band_name)s,%(user_id)s,%(music_genre)s,%(home_city)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
# ----- get all
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM bands
                   JOIN users on bands.user_id = users.id 
                   ;"""
        results = connectToMySQL(DATABASE).query_db(query)
        print("**********", results)
        bands = []
        for row in results:
            band=cls(row)
            band.poster = f"{row['first_name']} {row['last_name']}"
            bands.append(band)
        return bands
    
    @classmethod
    def get_user_bands(cls, data_dict):
        query = """SELECT * FROM bands
                   WHERE user_id = %(user_id)s
                   ;"""
        results = connectToMySQL(DATABASE).query_db(query, data_dict)
        bands = []
        for row in results:
            bands.append(cls(row))
        return bands
    
# ---- get one by id
    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM bands
                  JOIN users
                  ON bands.user_id = users.id
                  WHERE bands.id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        band = cls(result[0])
        band.poster = result[0]['first_name'] +" "+result[0]['last_name']
        return band
        
    #--- update
    @classmethod
    def update(cls, data_dict):
        query = """ UPDATE bands SET
         band_name = %(band_name)s, music_genre= %(music_genre)s, home_city= %(home_city)s WHERE id=%(id)s;
                   """
        return  connectToMySQL(DATABASE).query_db(query, data_dict)
   
    # ---delete
    @classmethod
    def delete(cls, data_dict):
        query = """ DELETE FROM bands WHERE id =%(id)s;"""
        return connectToMySQL (DATABASE).query_db(query,data_dict)


    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['band_name'])<2:
            is_valid =False
            flash("Band Name not valid", "band_name")
                
        if len(data_dict['music_genre'])<2:
            is_valid =False
            flash("Music Genre not valid", "music_genre")
        
        if len(data_dict["home_city"])<2:
            is_valid = False
            flash("Home City not valid", "home_city")

     
    
        return is_valid