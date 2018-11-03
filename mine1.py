__author__ = 'spowell'
import ec_psql_util
import logging
from flask import Flask
from flask import request
from flask_jsonpify import jsonpify as jsonify



logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s",
                    filename="flask_autocomplete.log",
                    filemode="w",
                    level=logging.DEBUG,
                    datefmt="%m/%d/%Y %I:%M:%S %p")

app = Flask(__name__)

list_streets = ec_psql_util.sql_get_full_address()

def find_autocomplete(_add_req, _list_streets):

    print(_add_req)

    list_candidates = list()
    for value in list_streets:
        if _add_req not in value["full_name"]:
            continue
        list_candidates.append(value)

    if 0 == list_candidates.__len__():
        print("none")
        return None
    else:
        return list_candidates


@app.route("/address", methods=["GET"])
def get_address():

    resp_candidates = find_autocomplete((request.args.get("add_req")).upper(), list_streets)

    return jsonify(resp_candidates)


if __name__ == '__main__':
    app.run(host="192.168.1.170", port=5000, debug=True)
