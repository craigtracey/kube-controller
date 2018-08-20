import json
import logging
import pprint

from flask import Flask, request
LOG = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/', methods=['POST', 'PUT'])
def index():
    LOG.info("Received: %s" % pprint.pprint(request.json))
    response = app.response_class(
        response=json.dumps({"status": {"success": "true"}, "children": []}),
        status=200,
        mimetype='application/json'
    )
    return response


def run_meta():
    app.run(host='0.0.0.0', port=8080)
