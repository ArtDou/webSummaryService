from flask import Flask, render_template, request, flash
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def formulaire():
    return render_template("formulaire.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacted")
def contacted():
    return "Votre formulaire a bien été envoyé."

#@app.route("/model")
#def model():
    

    
if __name__== '__main__':
    app.run(debug=True)