from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/countries/mali")
def mali():
    return render_template("mali.html")

@app.route("/regions/bamako")
def bamako_mali():
    return render_template("bamako_mali.html")

if __name__ == "__main__":
    app.run(debug=True)
