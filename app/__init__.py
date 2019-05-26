from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow





db = SQLAlchemy()
ma = Marshmallow()
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/imdb'

def create_app():
	# Configurations
	restapp = Flask(__name__)
	restapp.config.from_object('config')
	#mysqlconnection = mysql.getConnection(restapp)
	restapp.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
	restapp.config['SQLALCHEMY_ECHO'] = True
	restapp.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
	db.init_app(restapp)
	ma.init_app(restapp)
	return restapp
