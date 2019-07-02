from flask import *


def create_app():
	# Configurations
	restapp = Flask(__name__)
	restapp.config.from_object('config')
	return restapp
