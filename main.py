from flask import Flask, request, jsonify
from managing_directories_DB.managing_object_types.managing_object_type import Managing_object_type
from managing_directories_DB.managing_object_types.data_object_type import ObjectType

app = Flask(__name__)

client_service = Managing_object_type()


@app.route("/client", methods=["GET", "POST"])
def client():
    if request.method == "POST":
        data = request.json

        object_type = ObjectType(data["login"])
        err = client_service.add(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"body": {"test": data}}), 201
    elif request.method == "GET":
        return jsonify({"body": "GET"})


@app.route("/server", methods=["GET"])
def server():
    return jsonify({"body": "test"})


if __name__ == "__main__":
    app.run(port=5000)
