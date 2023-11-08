from flask import Flask, render_template, request, flash, redirect, url_for
from flask_httpauth import HTTPBasicAuth
import jinja2

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = 'secret key here'
users = {
    "yusuff":"kazeem"
}
@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("home.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if get_pw(username) == password:
            return render_template("secrets.html", username=username)
        else:
            flash('Please check your login details and try again.')
            return redirect(url_for("login_page"))



@app.route("/create", methods = ["GET", "POST"])
def create_page():
    if request.method == "GET":
        return render_template("createPassword.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        users[username] = password
        return redirect(url_for("login_page"))

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


if __name__ == "__main__":
    app.run(debug=True)