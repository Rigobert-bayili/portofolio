from flask import Flask, render_template
import requests

app = Flask(__name__)
app.secret_key = "basile2026"

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
    from flask import request, flash, redirect, url_for
    if request.method == "POST":
        nom = request.form["nom"]
        email = request.form["email"]
        message = request.form["message"]
        flash(f"Merci {nom} ! Votre message a bien été envoyé.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)