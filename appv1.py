from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home1():
    return 'hi there'

# @app.route("/base")
# def home():
#   return 

if __name__ == "__main__":
    app.run(debug=True)
    
    # run('', 8000, debug=True) change ports