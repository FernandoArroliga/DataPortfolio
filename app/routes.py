from app import app
from flask import render_template, request, jsonify
from chatbot_utils.chat import get_response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/blog_post")
def blog_post():
    return render_template("blog_post.html")

@app.route("/chatpage")
def chatpage():
    return render_template("chatpage.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    
    response = get_response(text)
    message = {"answer": response}
    
    return jsonify(message)

@app.route("/project_template")
def project_template():
    return render_template("project_template.html")