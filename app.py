from flask import Flask, render_template
from flask_migrate import Migrate
from dotenv import load_dotenv
from config import Config
from models.db import db
from models.user_model import User
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

if __name__ == "__main__":
    port = os.getenv('PORT')
    app.run(debug=True, port=port)

