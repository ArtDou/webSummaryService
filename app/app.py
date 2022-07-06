from flask import Flask, render_template, request
import requests


app = Flask(__name__)        

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/model", methods=['GET','POST'])
def model():
    text_to_summarize = request.form.get('input_text')
    
    if request.method == 'POST':
        model_port= 5000
        url = f"http://localhost:{model_port}/model/predict"
        headers = {"Content-Type": "application/json; charset=utf-8","accept": "application/json"}
        json = {"text":[text_to_summarize]}
        res = requests.post(url,  headers=headers, json=json)
        if res.status_code == 200:
            summary_text = res.text
        else:   
            summary_text =f"status_code:{res.status_code}"    
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
