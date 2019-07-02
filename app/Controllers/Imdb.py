from flask import request,make_response,Response
from flask_restful import Resource
from fynd_metrics import metrics_factory
from prometheus_client import CONTENT_TYPE_LATEST

class Imdb(Resource):
	def __init__(self):
		gen = metrics_factory.Metricsfactory()
		self.c = gen.generate_metric("Counter","search_hit_count","Tell search hit counts")
		print(self.c)

	# handle http get request
	def get(self):
		self.c.inc()
		data = {"message":"This is new movie data"}
		return {"data": data}, 200

class Metrics(Resource):

	def get(self):
		return Response(metrics_factory.generate_latest(), mimetype=CONTENT_TYPE_LATEST)