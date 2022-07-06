from flask import Flask, render_template, request
from sqlalchemy import create_engine, Table, Column, MetaData


app = Flask(__name__)

# Postgres username, password, and database name
POSTGRES_ADDRESS = '0.0.0.0' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'wym_admin'
POSTGRES_PASSWORD = 'admin'
POSTGRES_DBNAME = 'postgres-db'

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

meta = MetaData(db)
database = Table('user', meta,  
                       Column('nom', String),
                       Column('email', String),
                       Column('téléphone', String),
                       Column('commentaire', String))                  

with db.connect() as conn:

    # database.create() # METTRE UN IF TABLE EXIST ....
    insert_statement = database.insert().values(nom="Doctor Strange2", email="doctor.strange2@doctor.com")
    conn.execute(insert_statement)

    # Read
    select_statement = database.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)


@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/contact", methods=['GET','POST'])
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