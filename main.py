from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# My App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Added secret key for flash messages
db = SQLAlchemy(app)

# Database model
class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    plan = db.Column(db.String(20), nullable=False)
    menu_choices = db.Column(db.String(50), nullable=False)

# Route to handle form submissions and display records
@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        # Get the form data
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        plan = request.form.get('plan')
        menu_choices = ','.join(request.form.getlist('menu'))  # Handles checkboxes

        # Ensure menu_choices is not empty
        if not menu_choices:
            flash('Please select at least one menu choice.', 'error')
            return redirect(url_for('play'))

        # Create a new FormData entry and add it to the database
        new_entry = FormData(username=username, email=email, phone=phone, plan=plan, menu_choices=menu_choices)
        db.session.add(new_entry)
        db.session.commit()

        flash('Form submitted successfully!', 'success')
        return redirect(url_for('play'))

    # Fetch all the entries to display below the form
    entries = FormData.query.all()
    return render_template('play.html', entries=entries)

# Route to handle deleting a record
@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    entry = FormData.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted successfully!', 'success')
    return redirect(url_for('play'))

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

# Initialize database before the first request
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
