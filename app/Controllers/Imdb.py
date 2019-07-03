from flask import request,make_response,Response
from flask_restful import Resource
from fynd_metrics import metrics_factory
from prometheus_client import CONTENT_TYPE_LATEST
from .Constants import *


class Imdb(Resource):
	#def __init__(self):
		#gen = metrics_factory.MetricsObjectfactory()
		#self.c = gen.generate_metric("Counter","search_hit_count","Tell search hit counts")
		#print(self.c)

	# handle http get request
	def get(self):
		#self.c.inc()

		if request.args.get('movie') is not None:
			metrics_factory.MetricsObjectfactory().generate_counter_object(SEARCH_MOVIE_METRIC_COUNT_NAME,SEARCH_MOVIE_METRIC_COUNT_DESC,['movie_id','app_id']).labels(request.args.get('movie'),1).inc()
		elif request.args.get('actor') is not None:
			metrics_factory.MetricsObjectfactory().generate_counter_object(SEARCH_ACTOR_METRIC_COUNT_NAME,SEARCH_ACTOR_METRIC_COUNT_DESC,['actor_id']).labels(request.args.get('actor')).inc()
		else:
			metrics_factory.MetricsObjectfactory().generate_counter_object(SEARCH_METRIC_COUNT_NAME,SEARCH_METRIC_COUNT_DESC).inc()

		#common api hits made to app
		metrics_factory.MetricsObjectfactory().generate_counter_object(SEARCH_API_METRIC_COUNT_NAME,SEARCH_API_METRIC_COUNT_DESC).inc()

		#common gauge library
		metrics_factory.MetricsObjectfactory().generate_gauge_object(SEARCH_METRIC_GAUGE_NAME, SEARCH_METRIC_GAUGE_DESC).set('15')


		data = {"message":"This is new movie data"}
		return {"data": data}, 200

class Metrics(Resource):

	def get(self):
		return Response(metrics_factory.generate_latest(), mimetype=CONTENT_TYPE_LATEST)