from flask import Flask, render_template, request
import requests

from model import requests_model

from sqlalchemy import create_engine, Table, Column, String, MetaData, Integer, inspect
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

# https://www.compose.com/articles/using-postgresql-through-sqlalchemy/

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

# Postgres username, password, and database name
POSTGRES_ADDRESS = '0.0.0.0' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'wym_admin'
POSTGRES_PASSWORD = 'admin'
POSTGRES_DBNAME = 'postgres'

# A long string that contains the necessary Postgres login information
postgres_str = ('postgresql+psycopg2://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(
    username=POSTGRES_USERNAME,
    password=POSTGRES_PASSWORD,
    ipaddress=POSTGRES_ADDRESS,
    port=POSTGRES_PORT,
    dbname=POSTGRES_DBNAME))

# Create the connection
print(postgres_str)
db = create_engine(postgres_str)             

base = declarative_base()

# Définition de la classe de l'objet enregistrer dans la base de donnée
class User(base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key = True)
    nom = Column(String)
    email = Column(String)
    telephone = Column(String)
    texte = Column(String)
    resume = Column(String)

# Connection à la base de donnée
Session = sessionmaker(db)  
session = Session()

# Vérification de l'existence de la base de donnée
if not inspect(db).has_table('User'):
    base.metadata.create_all(db)

def add_entry_bdd(nom, email="", telephone="", texte="", resume=""):
    '''
    add_entry_bdd permet d'ajouter une entrée à la base de donnée\n
    Input:  
        * nom, email, telephone, texte, resume corespond au donnée du formulaire
    '''
    # Create 
    entry = User(nom=nom, email=email, telephone=telephone, texte=texte, resume=resume)  
    session.add(entry)  
    session.commit()

def read_all_bdd():
    '''
    read_all_bdd affiche la totalité de la base de donnée dans le terminal
    '''
    # Read
    emails = session.query(User)  
    for email in emails:  
        print(email)


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

@app.route("/contacted", methods= ['GET', 'POST'])
def contacted():
    name = request.form['nom']
    if request.method == 'POST': 
        print(name)       
        add_entry_bdd(nom=name)

    return render_template("contacted.html", nom=name) 

#@app.route("/model")
#def model():
 
if __name__== '__main__':
    app.run(debug=True, port=8000)
