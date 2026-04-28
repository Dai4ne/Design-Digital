from flask import Flask, render_template

app = Flask(__name__) #pega o nome do aplicativo que estou trabalhando

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__index__":
    app.run(debug=True)