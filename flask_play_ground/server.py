from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def index():
    return "hello from flask"

@app.route('/hi')                           
def hi():
    return "<h1> hi <h1> "

@app.route('/hi/<username>')                           
def hi_user(username):
    return f"<h1> hi {username} <h1> "


@app.route('/hi/<username>/<int:age>')                           
def user_info(username,age):
    return f"<h1> user name: {username} <br/> Age : {age} </h1> "
    

@app.route('/circles')                           
def circles():
    return render_template("index.html")


@app.route('/circles/<url_color>')                           
def colored_circles(url_color):
    print("*"*20, url_color, "*"*20)
    return render_template("index.html", color=url_color)

if __name__ == "__main__":
    app.run(debug=True) 