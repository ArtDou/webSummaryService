from flask import Flask, render_template, request
import requests
from model import requests_model

app = Flask(__name__)        

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/model", methods=['GET','POST'])
def model():
    text_to_summarize = request.form.get('input_text')
    
    if request.method == 'POST':
       
       summary_text = requests_model(text_to_summarize)
    else: 
        summary_text ="no text to summarized"
    return render_template("model.html", text=text_to_summarize, summary=summary_text)

@app.route("/contact", methods=['GET','POST'])
def formulaire():
    return render_template("formulaire.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacted")
def contacted():  
    return "Votre formulaire a bien été envoyé."
 
if __name__== '__main__':
    app.run(debug=True, port=8000)
