from re import A
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)


@app.route("/")
def index(): 
    return render_template("index.html")



@app.route("/1")

def employment():
        return render_template("employment.html")

@app.route("/2")
def upcoming():
        return render_template("upcomingProjects.html")

@app.route("/3")
def currentproj():
        return render_template("currentProjects.html")
    



@app.route("/<usr>")
def user(usr):
    
        return f"<h1>{usr}<h1>"





if __name__ == "__main__":
    app.run(debug=True)