from flask import Flask, request, url_for, render_template
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = ''
spaces3 = """
        """

@app.route('/')
def hello_person():
	return render_template('home.html')
	<form class="form1" method="POST" action="%s"><input name="person" /><input type="submit" value="Continue" /></form>
	

@app.route('/greet', methods=['POST'])
def greet():
    global personne
    personne = request.form["person"]
    greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return render_template('greet.html')

@app.route('/intro')
def intro():
    global personne
    global spaces3
    return render_template('intro.html')
    #intro = paragraph"

@app.route('option1')
def option1():
    #option1 =  page of option 1
    return render_template('option1')

@app.route('/static/option2')
def option2():
    global personne
