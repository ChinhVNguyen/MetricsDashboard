import logging
from flask import Flask, render_template, request, jsonify
from flask_opentracing import FlaskTracing
from prometheus_flask_exporter import PrometheusMetrics
from jaeger_client import Config
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

import pymongo
from flask_pymongo import PyMongo

logging.basicConfig(level=logging.INFO)
logging.info("LOGLEVEL INFO")

app = Flask(__name__)
metrics = PrometheusMetrics(app)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)

def init_tracer(service):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
            'reporter_batch_size': 1,
        },
        service_name=service
    )
    return config.initialize_tracer()

tracer = init_tracer("backend-app")
tracing = FlaskTracing(tracer, True, app)


@app.route("/")
def homepage():
    with tracer.start_span("homepage") as span:
        span.set_tag("endpoint", "/")
        return "Hello World"


@app.route("/api")
def my_api():
    with tracer.start_span("my_api") as span:
        answer = "something"
        span.set_tag("response", answer)
        return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    with tracer.start_span("add_star") as span:
        # Extracting the data from the request
        try:
            star = mongo.db.stars
            name = request.json["name"]
            distance = request.json["distance"]

            # Set tags for tracing
            span.set_tag("name", name)
            span.set_tag("distance", distance)

            # Insert into the database
            star_id = star.insert({"name": name, "distance": distance})
            new_star = star.find_one({"_id": star_id})

            output = {"name": new_star["name"], "distance": new_star["distance"]}
            return jsonify({"result": output})

        except KeyError as e:
            # Log an error span if the expected data is missing
            span.set_tag("error", True)
            span.log_kv({"event": "error", "error.object": str(e)})
            return jsonify({"error": f"Missing parameter: {str(e)}"}), 400


if __name__ == "__main__":
    app.run()
