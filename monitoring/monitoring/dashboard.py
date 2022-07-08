import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine, Table, Column, String, MetaData, Integer, inspect
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from PIL import Image
import pandas as pd
import os
import base64

# Postgres username, password, and database name
POSTGRES_ADDRESS = 'wym_db' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
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

# Page layout   
st.set_page_config(layout="wide")

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code

gif_html = get_img_with_href('./monitoring/WYM_image.png', 'https://fr.wikipedia.org/wiki/Pulp_Fiction')


colp1, colp2, colp3 = st.columns([5, 20, 5])
# -- Put the image in the middle column
with colp2:
    # image = Image.open("./monitoring/WYM_image.png")
    st.markdown(gif_html, unsafe_allow_html=True)

# -- Create three columns
col1, col2, col3 = st.columns([5, 20, 5])
#-- Put the title in the last column
with col2:
    st.title("WYM\n")
    st.title("Welcome, You Motherf***er")
# -- We use the first column here as a dummy to add a space to the left

colq1, name_col, colq3 = st.columns([5, 5, 5])

# -- Read in the data
data = pd.read_sql("""SELECT * FROM "Users" """, db)
list_name = data.nom.unique().tolist()
list_name.insert(0,'All')
with name_col:
    name_choice = st.selectbox(
        "What user would you like to look at?",
        list_name,
    )

# -- Apply the name filter chosed by user
filtered_df = data.copy()
if name_choice != "All":
    filtered_df = filtered_df[filtered_df.nom == name_choice]
filtered_df["text_length"] = filtered_df.texte.map(lambda x:len(x))
filtered_df["resume_length"] = filtered_df.resume.map(lambda x:len(x))
# -- Create the figure in Plotly
fig = px.line(filtered_df.sort_values("text_length"),
    x="text_length",
    y="resume_length",
    text="nom"
)
fig.update_traces(mode="markers+lines")
fig.update_layout(title="resume length in function of text length")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig, use_container_width=True)





# # ---------------------- Demo
# # -- Get the user input
# year_col, continent_col, log_x_col = st.columns([5, 5, 5])
# with year_col:
#     year_choice = st.slider(
#         "What year would you like to examine?",
#         min_value=1952,
#         max_value=2007,
#         step=5,
#         value=2007,
#     )
# with continent_col:
#     continent_choice = st.selectbox(
#         "What continent would you like to look at?",
#         ("All", "Asia", "Europe", "Africa", "Americas", "Oceania"),
#     )
# with log_x_col:
#     log_x_choice = st.checkbox("Log X Axis?")
# # -- Read in the data
# df = px.data.gapminder()
# # -- Apply the year filter given by the user
# filtered_df = df[(df.year == year_choice)]
# # -- Apply the continent filter
# if continent_choice != "All":
#     filtered_df = filtered_df[filtered_df.continent == continent_choice]
# # -- Create the figure in Plotly
# fig = px.scatter(
#     filtered_df,
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",
#     color="continent",
#     hover_name="country",
#     log_x=log_x_choice,
#     size_max=60,
# )
# fig.update_layout(title="GDP per Capita vs. Life Expectancy")
# # -- Input the Plotly chart to the Streamlit interface
# st.plotly_chart(fig, use_container_width=True)