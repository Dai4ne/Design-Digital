import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template

app = Flask(__name__, 
            template_folder='../src/templates', 
            static_folder='../src/static')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/quem')
def quem():
    return render_template('quem.html')