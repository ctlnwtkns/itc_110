personne = ''
spaces3 = """
        """

@app.route('/')
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
    return render_template('intro.html', greet, personne)

@app.route('/option1')
def option1():
    return render_template('option1.html')

@app.route('/option2')
def option2():
    global personne
    return(option2, personne)
    return render_template('option2.html')

if __name__ == '__main__':
    app.run(debug=True)
