from app import create_app
from flask import Blueprint
from flask_restful import Api
from app.Controllers.Imdb import Imdb

# create app instance
my_app = create_app()

api_bp = Blueprint('api', __name__)

api = Api(my_app)
# my_app.register_blueprint(api_bp, url_prefix='/v1')

# register routes with resources
api.add_resource(Imdb, '/search', endpoint='get')
api.add_resource(Imdb, '/movie', endpoint='put')
api.add_resource(Imdb, '/movie/<int:movieid>', endpoint='delete')

# start app on specified port
my_app.run(host='0.0.0.0', port=3000, debug=True)