from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img

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

# TODO: acknowledgements page


nav.init_app(app)
if __name__ == '__main__':
    app.run(debug=True)