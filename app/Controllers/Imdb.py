from flask import request
from flask_restful import Resource
from app.Models.Movies import Movies


class Imdb(Resource):

	# handle http get request
	def get(self):
		data = Movies.getAll(self)
		return {"data": data}, 200

	# handle http post request
	def post(self):
		postMovieData = request.get_json(force=True)
		response = Movies.add(postMovieData)
		if response[0] == 1:
			return {"msg":"Record added successfully"}, 201
		else:
			return {"msg":"Failed to add data"},406

	# handle http delete request
	def delete(self,movieid):
		if valid_(email_str):
			return email_str
		else:
			raise ValueError('{} is not a valid email'.format(email_str))
		response = Movies.delete(movieid)
		if response[0] == 1:
			return {"msg":"Record deleted successfully"}, 200
		elif response[0] == -1:
			return {"msg":response[1]}, 406
		elif response[0] == 0:
			return {"msg":"Record Not found"}