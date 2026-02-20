from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
users = {}  # Simple in-memory storage

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        users[username] = generate_password_hash(password)
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            return "Login Successful!"
        else:
            return "Login Failed!"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)