from Desafio01 import app 
from flask import render_template 

@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/quem')
def quem():
    return render_template('quem.html')