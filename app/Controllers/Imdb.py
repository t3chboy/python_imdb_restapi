from flask import request,make_response,Response
from flask_restful import Resource
from fynd_metrics import metrics_factory
from fynd_exception import fynd_exception as fe
from prometheus_client import CONTENT_TYPE_LATEST
from .Constants import *
import time
import sys,traceback


#histogram
apih = metrics_factory.MetricsObjectFactory().generate_histogram_object(SEARCH_API_METRIC_HISTOGRAM_NAME,SEARCH_API_METRIC_HISTOGRAM_DESC,['api','method'])
ab = apih.labels("abc","get")

class Imdb(Resource):
	#def __init__(self):
	#gen = metrics_factory.MetricsObjectFactory()
	#self.c = gen.generate_metric("Counter","search_hit_count","Tell search hit counts")
	#print(self.c)

	# handle http get request
	def get(self):
		#self.c.inc()
		try:
			if request.args.get('movie') is not None:
				metrics_factory.MetricsObjectFactory().generate_counter_object(SEARCH_MOVIE_METRIC_COUNT_NAME,SEARCH_MOVIE_METRIC_COUNT_DESC,['movie_id','app_id']).labels(request.args.get('movie'),1).inc()
			elif request.args.get('actor') is not None:
				metrics_factory.MetricsObjectFactory().generate_counter_object(SEARCH_ACTOR_METRIC_COUNT_NAME,SEARCH_ACTOR_METRIC_COUNT_DESC,['actor_id']).labels(request.args.get('actor')).inc()
			else:
				metrics_factory.MetricsObjectFactory().generate_counter_object(SEARCH_METRIC_COUNT_NAME,SEARCH_METRIC_COUNT_DESC).inc()

			#common api hits made to app
			metrics_factory.MetricsObjectFactory().generate_counter_object(SEARCH_API_METRIC_COUNT_NAME,SEARCH_API_METRIC_COUNT_DESC).inc()

			#common gauge library
			metrics_factory.MetricsObjectFactory().generate_gauge_object(SEARCH_METRIC_GAUGE_NAME, SEARCH_METRIC_GAUGE_DESC).set('15')


			data = {"message":"This is new movie data"}
			#time.sleep(200)
			print("Headers : ",request.headers)
			return {"data": data}, 200
		except Exception as e:
			fe.FyndCuctsomException(e,"None")

	def post(self):
		print("Headers : ", request.headers)
		return{"success":"Added successfully"},200

class Metrics(Resource):

	#@ab.time()
	def get(self):
		return Response(metrics_factory.generate_latest(), mimetype=CONTENT_TYPE_LATEST)