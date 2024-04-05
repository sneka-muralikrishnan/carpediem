from flask import Flask, render_template, request, redirect, url_for, send_file
app = Flask(__name__)
user = {
    "sairam":12345,
        "sneka":12345,
            "philo":12345,
                "sai":12345,

}
@app.route("/")
def index():
    return render_template("Welcome.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/image", methods=["POST"])
def image():
    username = request.form["username"]
    password = request.form["password"]
    try:
        if username in user:
            if password==12345:
                print("done")
                return render_template("/image.html")
        else:
            error = "Invalid username or password. Please try again."
            return render_template("/login.html", error=error)
    except:
        return "error"
        
    
@app.route("/imageupload")
def imageupload():
    return render_template("image.html")  
        

@app.route("/comment")
def comment():
    return render_template("comment.html")

if __name__ == "__main__":
    app.run(debug=True)