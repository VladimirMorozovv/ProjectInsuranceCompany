from flask import Flask, request, jsonify
from managing_directories_DB.managing_object_types.managing_object_type import Managing_object_type
from managing_directories_DB.managing_object_types.data_object_type import ObjectType
from managing_directories_DB.customer_management.customer_managment import CustomerFL_managment, CustomerL_managment
from managing_directories_DB.customer_management.data_clients import ClientFL, ClientL
from managing_directories_DB.managing_object.managing_object import Managing_object
from managing_directories_DB.managing_object.data_object import Object
from managing_directories_DB.policy_management.policy_management import Policy_managment
from managing_directories_DB.policy_management.data_policy import Policy, SellPolicy

from reports.report1 import Report_development1


app = Flask(__name__)

managing_object_type = Managing_object_type()
customerFL_managment = CustomerFL_managment()
customerL_managment = CustomerL_managment()
managing_object = Managing_object()
policy_managment = Policy_managment()

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

@app.route("/object_type", methods=["POST", "PUT", "DELETE"])
def object():
    if request.method == "POST":
        data = request.json

        object_type = Object(data["Name"], data["numberPassport"], data["idTypeObject"])
        err = managing_object.add(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Данные успешно внесены в базу"}), 201
    elif request.method == "PUT":
        data = request.json

        object_type = Object(data["Name"], data["numberPassport"], data["idTypeObject"], data["idObjects"])
        err = managing_object.change(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201

    elif request.method == "DELETE":
        data = request.json

        object_type = Object(None, None, None, data["id"])
        err = managing_object.delete(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Данные успешно удалены"}), 201


@app.route("/policy", methods=["POST", "PUT", "PUTCH"])
def polic():
    if request.method == "POST":
        data = request.json
        if data["idL"]== "None":


            policy = Policy(data["didTypeObject"], data["idObjects"], data["startDate"], data["stopDate"],
                            data["insuranceAmount"], data["idFL"])
            err = policy_managment.add(policy)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно внесены в базу"}), 201
        elif data["idFL"] == "None":

            policy = Policy(data["didTypeObject"], data["idObjects"], data["startDate"], data["stopDate"],
                            data["insuranceAmount"], None, data["idL"])
            err = policy_managment.add(policy)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно внесены в базу"}), 201
        elif request.method == "PUT":
            data = request.json

    elif request.method == "PUT":
        data = request.json

        if data["idL"] == "None":

            policy = Policy(data["didTypeObject"], data["idObjects"], data["startDate"], data["stopDate"],
                            data["insuranceAmount"], data["idFL"], None, data["policyNumber"])
            err = policy_managment.change(policy)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201
        elif data["idFL"] == "None":

            policy = Policy(data["didTypeObject"], data["idObjects"], data["startDate"], data["stopDate"],
                            data["insuranceAmount"], None, data["idL"], data["policyNumber"])
            err = policy_managment.change(policy)
            if err is not None:
                return jsonify({"body": "error"}), 500
            else:
                return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201


    elif request.method == "PUTCH":
        data = request.json

        policy = SellPolicy(data["policyNumber"], data["status"])
        err = policy_managment.sell(policy)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Продажа исполнена"}), 201

@app.route("/report", methods=["GET"])
def all_report():

    if request.args['name']=='report1':

        report_one = Report_development1(request.args['datestart'], request.args['datestart'])
        err = report_one.processing_report(report_one.data_start, report_one.data_stop)

        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return , 201
    elif request.method == "PUT":
        data = request.json

        object_type = Object(data["Name"], data["numberPassport"], data["idTypeObject"], data["idObjects"])
        err = managing_object.change(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Данные успешно изменены"}), 201

    elif request.method == "DELETE":
        data = request.json

        object_type = Object(None, None, None, data["id"])
        err = managing_object.delete(object_type)
        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return jsonify({"status": "success", "text": "Данные успешно удалены"}), 201



if __name__ == "__main__":
    app.run(port=5000)
