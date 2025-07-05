from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = "user_data.json"

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        user_data = {
            "username": request.form.get("username"),
            "discord_id": request.form.get("discord_id"),
            "email": request.form.get("email")
        }
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(user_data)

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

        return redirect("/success")
    return render_template("form.html")

@app.route("/success")
def success():
    return "申し込みありがとうございます！"

if __name__ == "__main__":
 port = int(os.environ.get("PORT", 80808))
 app.run(host="0.0.0.0", port=port)
