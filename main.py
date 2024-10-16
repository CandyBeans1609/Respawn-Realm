from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

# My App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Data Class
class MyDatabase(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.BigInteger, nullable=False)
    plan = db.Column(db.String(150), nullable=False)
    snacks = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"Booking for {self.username}"

# Route for index.html
@app.route("/")
def index():
    return render_template("index.html")

# Route for play.html
@app.route("/play", methods=["POST","GET"])
def play():
    # Add
    if request.method == "POST":
        current_task = request.form
    #Display

    return render_template("play.html")


# Route for menu.html
@app.route("/menu")
def menu():
    return render_template("menu.html")

# Route for pricing.html
@app.route("/pricing")
def pricing():
    return render_template("pricing.html")



if __name__ == "__main__":  # Fixing a minor error in your condition
    with app.app_context():
        db.create_all()
    app.run(debug=True)

