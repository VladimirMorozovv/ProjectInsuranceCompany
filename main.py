from flask import Flask, request, jsonify
from managing_directories_DB.managing_object_types.managing_object_type import Managing_object_type
from managing_directories_DB.managing_object_types.data_object_type import ObjectType
from managing_directories_DB.customer_management.customer_managment import CustomerFL_managment, CustomerL_managment
from managing_directories_DB.customer_management.data_clients import ClientFL, ClientL

app = Flask(__name__)

managing_object_type = Managing_object_type()
customerFL_managment = CustomerFL_managment()
customerL_managment = CustomerL_managment()



@app.route("/object_type", methods=["POST", "PUT", "DELETE"])
def type():
    if request.method == "POST":
        data = request.json

        object_type = ObjectType(data["ObjectType"])
        err = managing_object_type.add(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Данные успешно внесены в базу"}), 201
    elif request.method == "PUT":
        data = request.json

        object_type = ObjectType(data["ObjectType"], data["idTypes"])
        err = managing_object_type.change(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201

    elif request.method == "DELETE":
        data = request.json

        object_type = ObjectType(None, data["id"])
        err = managing_object_type.delete(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Данные успешно удалены"}), 201


@app.route("/client", methods=["POST", "PUT", "DELETE"])
def man_client():
    if request.method == "POST":
        data = request.json
        if data["legal"] == "False":

            client = ClientFL(data["FIO"], data["residentialAddress"],  data["numberPassport"], data["numberPhone"])
            err = customerFL_managment.add(client)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно внесены в базу"}), 201
        elif data["legal"] == "True":

            client = ClientL(data["Name"], data["legalAddress"],  data["OGRN"], data["numberPhone"])
            err = customerL_managment.add(client)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно внесены в базу"}), 201
    elif request.method == "PUT":
        data = request.json

        if data["legal"] == "False":

            client = ClientFL(data["FIO"], data["residentialAddress"], data["numberPassport"], data["numberPhone"], data["id"])
            err = customerFL_managment.change(client)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201
        elif data["legal"] == "True":

            client = ClientL(data["Name"], data["legalAddress"], data["OGRN"], data["numberPhone"], data["id"])
            err = customerL_managment.change(client)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201

    elif request.method == "DELETE":
        data = request.json

        if data["legal"] == "False":

            client = ClientFL(None, None, None, None, data["id"])
            err = customerFL_managment.delete(client)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201
        elif data["legal"] == "True":

            client = ClientL(None, None, None, None, data["id"])
            err = customerL_managment.delete(client)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201


if __name__ == "__main__":
    app.run(port=5000)
