from flask import Flask, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = ''
spaces3 = """
        """

@app.route('/')
def hello_person():
	return % (url_for('greet'),)



@app.route('/greet', methods=['POST'])
def greet():
    global personne
    personne = request.form["person"]
    greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return % (greet, personne, url_for('intro'))

@app.route('/intro')
def intro():
    global personne
    global spaces3
    intro = 
