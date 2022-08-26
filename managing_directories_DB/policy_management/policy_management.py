import config
import data_policy
import mysql.connector


class Policy_managment:

    def add(self, policy: data_policy.Policy):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                if policy.idFL:
                    add_policy = f"""
                        INSERT INTO insurancePolicyClient
                        (idTypeObject, idFL, idL, idObjects, startDate, stopDate, insuranceAmount, costInsurance, status)
                        VALUES
                        ({policy.idTypeObject}, {policy.idFL}, NULL, {policy.idObjects}, '{policy.startDate}', 
                        '{policy.stopDate}', {policy.insuranceAmount}, insuranceAmount/100*10, 'atWork');
                    """
                else:
                    add_policy = f"""
                        INSERT INTO insurancePolicyClient
                        (idTypeObject, idFL, idL, idObjects, startDate, stopDate, insuranceAmount, costInsurance, status)
                        VALUES
                        ({policy.idTypeObject}, NULL, {policy.idFL}, {policy.idObjects}, '{policy.startDate}', 
                        '{policy.stopDate}', {policy.insuranceAmount}, insuranceAmount/100*10, 'atWork')
                    """

                with connection.cursor() as cursor:
                    cursor.execute(add_policy)
                    connection.commit()
        except Exception as e:
            return e

    def change(self, policy: data_policy.Policy):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                if policy.idFL:
                    change_policy = f"""
                        UPDATE insurancePolicyClient SET idTypeObject ={policy.idTypeObject}, idFL = {policy.idFL}, 
                        idL = NULL, idObjects = {policy.idObjects}, startDate= '{policy.startDate}', 
                        stopDate = '{policy.stopDate}', insuranceAmount = {policy.insuranceAmount}
                        WHERE policyNumber = {policy.policyNumber}
                    """
                with connection.cursor() as cursor:
                    cursor.execute(change_policy)
                    connection.commit()
        except Exception as e:
            return e

    def sell(self, sell_policy: data_policy.SellPolicy):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_cleintsFL = f"""
                    UPDATE insurancePolicyClient SET status = '{sell_policy.status}'
                    WHERE policyNumber = {sell_policy.policyNumber};
                """
                with connection.cursor() as cursor:
                    cursor.execute(delete_cleintsFL)
                    connection.commit()
        except Exception as e:
            return e