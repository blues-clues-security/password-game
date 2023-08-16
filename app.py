from flask import Flask, render_template, request
import password_game  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    next_rule = ""
    password = ""
    satisfied_rules = []
    sponsor_images = {}
    if request.method == "POST":
        password = request.form["password"]
        message, next_rule, satisfied_rules, sponsor_images = password_game.main(password)

    return render_template("index.html", message=message, next_rule=next_rule, password=password, satisfied_rules=satisfied_rules, sponsor_images=sponsor_images)

if __name__ == "__main__":
    app.run(debug=True)
