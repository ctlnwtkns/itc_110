from flask import Flask, request, render_template
#import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = ''
spaces3 = """
        """

@app.route('/')
#def hello_person():

def home():
	return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    global personne
    personne = request.form["person"]
    #greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return render_template('greet.html')

@app.route('/intro')
def intro():
    global personne
    global spaces3
    return render_template('intro.html, greet, personne')
    #intro = paragraph"

@app.route('/option1')
def option1():
    #option1 =  page of option 1
    return render_template('option1')

@app.route('/option2')
def option2():
    global personne
    return(option2, personne)
    return render_template('option2.html')
