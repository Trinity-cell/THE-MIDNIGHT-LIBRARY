from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create a database on a relative path
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

# Create an instance of a database
db = SQLAlchemy(app)

# The database models are created using classes
# This is a database for our user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False) # 60 chars because of hashing algorithm
    reason = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/join", methods=['GET', 'POST'])
def join():
    if request.method == "POST":
        # storing the data from the form in variables
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        reason = request.form['reason']

        new_user = User(
            # putting the data from the form into the user database
            username = name,
            email = email,
            password = password,
            reason = reason
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('library'))
    return render_template("signup.html")

@app.route("/library")
def library():
    return render_template("library.html")

if __name__ == "__main__":
    app.run(debug=True)

