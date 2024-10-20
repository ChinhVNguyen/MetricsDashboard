from flask import Flask, json, render_template
from prometheus_flask_exporter import PrometheusMetrics
import logging
from jaeger_client import Config
from flask_opentracing import FlaskTracing

logging.basicConfig(level=logging.INFO)
logging.info("LOGLEVEL INFO")

app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.info("app_info", "Backend Application", version="1.0.0")

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
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
