from flask import Flask, render_template
from config import Config
from models.db import db
from models.user_model import user

import os

db.init_app(app)

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5055))
    app.run(debug=True, port=port)

