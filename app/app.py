from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLACLHEMY_DATABASE_URI']='postgresql://wym_admin:admin@localhost/postgres-db'

db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__='BDD'
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String)
    téléphone=db.Column(db.String)
    email=db.Column(db.String)
    commentaire=db.Column(db.String)

    def __init__(self, nom, téléphone, email, commentaire):
        self.nom=nom
        self.téléphone=téléphone
        self.email=email
        self.commentaire=commentaire


@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def formulaire():

    if request.method =='POST':
        nom=request.form['nom']
        téléphone=request.form['téléphone']
        email=request.form['email']
        commentaire=request.form['commentaire']

    data=Data(nom, téléphone, email, commentaire)
    db.session.add(data)
    db.session.commit()

    return render_template("formulaire.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacted", methods=['GET'])
def contacted():  

    return "Votre formulaire a bien été envoyé."

#@app.route("/model")
#def model():
    

    
if __name__== '__main__':
    app.run(debug=True)