from app import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/web_scraping_gui")
def web_scraping_gui():
    return render_template("web_scraping_gui.html")

@app.route("/project_template")
def project_template():
    return render_template("project_template.html")