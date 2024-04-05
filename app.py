from flask import Flask, render_template, request, redirect, url_for, send_file
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("Welcome.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/comment")
def comment():
    return render_template("comment.html")

if __name__ == "__main__":
    app.run(debug=True)