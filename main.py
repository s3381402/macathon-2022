from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img
from flask_sqlalchemy import SQLAlchemy

# database
db = SQLAlchemy()
DB_NAME = "database.db"

# topbar logo
logo = img(src='./static/images/logo.png', height="50", width="50", style="margin-top:-15px")

# navbar menu items
topbar = Navbar(logo,
                # View('Login', 'login'),
                View('Home', 'home'),
                View('Map', 'map'),
                View('Report Issue', 'report_issue'),
                # View('Acknowledgements', 'acknowledgements'),
                )

nav = Nav()
nav.register_element('top', topbar)
app = Flask(__name__)
Bootstrap(app)
app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # sqlite/sqlalchemy databse is stored at sqlite:///DB_NAME
db.init_app(app) # Linking db to app


# TODO: login page

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Map page
@app.route("/map")
def map():
    return render_template("map.html")

# Report Issue page
@app.route("/report_issue")
def report_issue():
    return render_template("report_issue.html")

@app.route('/', methods=['POST'])
def report_form():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text
    
# TODO: acknowledgements page


nav.init_app(app)
if __name__ == '__main__':
    app.run(debug=True)