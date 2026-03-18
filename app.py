from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Configuration Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'basilebayili@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'basilebayili@gmail.com'

mail = Mail(app)

GITHUB_USERNAME = "Rigobert-bayili"

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projets")
def projets():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?sort=updated&per_page=100"
    response = requests.get(url)
    repos = response.json()
    return render_template("projets.html", repos=repos)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nom = request.form["nom"]
        email = request.form["email"]
        message = request.form["message"]
        try:
            msg = Message(
                subject=f"Message de {nom} via Portfolio",
                recipients=["basilebayili@gmail.com"],
                body=f"Nom : {nom}\nEmail : {email}\n\nMessage :\n{message}"
            )
            mail.send(msg)
            flash(f"Merci {nom} ! Votre message a bien été envoyé.", "success")
        except Exception as e:
            flash("Erreur lors de l'envoi. Réessayez plus tard.", "danger")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.route("/cv")
def cv():
    return send_from_directory("static", "CV_BAYILI_Basile_Data_SPECIALISTE.pdf")

if __name__ == "__main__":
    app.run(debug=True)