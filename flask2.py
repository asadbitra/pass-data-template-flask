#passing data/variables to html templates
#Lets import flask first
from flask import Flask
#Lets import Render_templates
from flask import render_template
#Lets create an app now
app = Flask(__name__)
#lets create our first route
@app.route('/')
#lets create a function for our route
def index():
    #Now I am creating a variable and I will pass it to my html template
    name = "gul khan"
    return render_template('index.html', name=name)
    #name = name is the data I want to pass 
#Now I will create function to run app
app.run(debug=True, port=8080)
#Now I will create a template folder and inside it a html file
# Then I will display my data/name sent from backend.