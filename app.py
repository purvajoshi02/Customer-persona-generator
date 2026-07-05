from flask import Flask, render_template, request
from utils.gemini import generate_persona

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    persona = None

    if request.method == "POST":

        data = {
            "name": request.form.get("name"),
            "age": request.form.get("age"),
            "occupation": request.form.get("occupation"),
            "income": request.form.get("income"),
            "interests": request.form.get("interests"),
            "goals": request.form.get("goals"),
            "challenges": request.form.get("challenges")
        }

        persona = generate_persona(data)

    return render_template(
        "index.html",
        persona=persona
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
