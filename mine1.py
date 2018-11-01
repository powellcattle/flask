from flask import Flask
from flask_jsonpify import jsonpify as jsonify
from flask_responses import json_response

app = Flask(__name__)


@app.route("/address", methods=["GET"])
def get_address():
    alist = list()
    alist.append({"address": "107 E CALHOUN ST"})
    alist.append({"address": "428 MADRONA RANCH RD"})
    full_dict = dict()
    full_dict["street_adresses"] = alist
    # return(jsonify(full_dict))

    return jsonify(full_dict)



if __name__ == '__main__':
    app.run(host="192.168.1.170", port=5000, debug=True)
