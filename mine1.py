from flask import Flask
from flask_jsonpify import jsonpify as jsonify
from flask_responses import json_response

app = Flask(__name__)
alist = list()


def sql_get_full_address():
    alist.append({"full_name": "107 E CALHOUN ST"})
    alist.append({"full_name": "428 MADRONA RANCH RD"})


@app.route("/address", methods=["GET"])
def get_address():
    if alist.__len__() == 0:
        sql_get_full_address()

    #
    # full_dict = dict()
    # full_dict["street_adresses"] = alist
    # # return(jsonify(full_dict))

    return jsonify(alist)



if __name__ == '__main__':
    app.run(host="192.168.1.170", port=5000, debug=True)
