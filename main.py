import os.path

from flask import Flask, request, jsonify, send_from_directory

from managing_directories_DB.managing_object_types.managing_object_type import Managing_object_type
from managing_directories_DB.managing_object_types.data_object_type import ObjectType
from managing_directories_DB.customer_management.customer_managment import CustomerFL_managment, CustomerL_managment
from managing_directories_DB.customer_management.data_clients import ClientFL, ClientL
from managing_directories_DB.managing_object.managing_object import Managing_object
from managing_directories_DB.managing_object.data_object import Object
from managing_directories_DB.policy_management.policy_management import Policy_managment
from managing_directories_DB.policy_management.data_policy import Policy, SellPolicy

from reports.report1 import Report_development1
from reports.report2 import Report_development2
from reports.report3 import Report_development3
from reports.report4 import Report_development4
from reports.report5 import Report_development5
from reports.report6 import Report_development6

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

    if str(request.args['name'])=='report1':

        report_one = Report_development1(request.args['datestart'], request.args['datestop'])
        err = report_one.processing_report(str(report_one.data_start), str(report_one.data_stop))

        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return send_from_directory(directory=os.path.dirname(os.path.abspath(__file__)), path='report1_result.txt')

    elif str(request.args['name']) == 'report2':

        report_two = Report_development1(request.args['datestart'], request.args['datestop'])
        err = report_two.processing_report(str(report_two.data_start), str(report_two.data_stop))

        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return send_from_directory(directory=os.path.dirname(os.path.abspath(__file__)), path='report2_result.txt')

    elif str(request.args['name']) == 'report3':

        report_three = Report_development3(request.args['clientid'])
        err = report_three.processing_report(str(report_three.id))

        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return send_from_directory(directory=os.path.dirname(os.path.abspath(__file__)), path='report3_result.txt')


    elif str(request.args['name']) == 'report4':

        report_four = Report_development4()
        err = report_four.processing_report()

        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return send_from_directory(directory=os.path.dirname(os.path.abspath(__file__)), path='report4_result.txt')

    elif str(request.args['name']) == 'report5':

        report_five = Report_development5()
        err = report_five.processing_report()

        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return send_from_directory(directory=os.path.dirname(os.path.abspath(__file__)), path='report5_result.txt')

    elif str(request.args['name']) == 'report6':

        report_six = Report_development6()
        err = report_six.profitability()

        if err is not None:
            return jsonify({"body": "error"}), 500
        else:
            return send_from_directory(directory=os.path.dirname(os.path.abspath(__file__)), path='report6_result.txt')



if __name__ == "__main__":
    app.run(port=5000)
