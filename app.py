from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "basile2026"

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projets")
def projets():
    return render_template("projets.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nom = request.form["nom"]
        email = request.form["email"]
        message = request.form["message"]
        flash(f"Merci {nom} ! Votre message a bien été envoyé.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)