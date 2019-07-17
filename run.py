from app import create_app
from flask import *
from flask_restful import Api
from app.Controllers.Imdb import Imdb,Metrics

# create app instance
my_app = create_app()

api_bp = Blueprint('api', __name__)

api = Api(my_app)
# my_app.register_blueprint(api_bp, url_prefix='/v1')

# register routes with resources
api.add_resource(Metrics,'/metrics')
api.add_resource(Imdb, '/myntra_search', endpoint='get')
api.add_resource(Imdb, '/myntra_add', endpoint='post')



# start app on specified port
my_app.run(host='0.0.0.0', port=8001, debug=True)