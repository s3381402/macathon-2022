from flask import Flask, render_template

app = Flask(__name__)

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
