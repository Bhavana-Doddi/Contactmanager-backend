from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app=Flask(__name__)
CORS(app, origins=["https://contactmanager-frontend.onrender.com"], supports_credentials=True, methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])



app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db= SQLAlchemy(app)
