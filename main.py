from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# My App
app = Flask(__name__)

# Route for index.html
@app.route("/")
def index():
    return render_template("index.html")

# Route for menu.html
@app.route("/menu")
def menu():
    return render_template("menu.html")

# Route for pricing.html
@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

if __name__ == "__main__":  # Fixing a minor error in your condition
    app.run(debug=True)
