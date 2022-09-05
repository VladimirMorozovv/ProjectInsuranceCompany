import config
import mysql.connector


class Report_development5:
    def __init__(self):
        self.mistake = ''

    def processing_report(self):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_profitability = f"""SELECT objectsInsurance.idObjects, objectsInsurance.Name, 
                                        objectsInsurance.numberPassport, insurancePolicyClient.insuranceAmount
                                        FROM insurancePolicyClient, objectsInsurance
                                        WHERE objectsInsurance.idObjects = insurancePolicyClient.idObjects
                                        GROUP BY insurancePolicyClient.insuranceAmount, objectsInsurance.Name, 
                                        objectsInsurance.numberPassport, objectsInsurance.idObjects
                                        ORDER BY insuranceAmount DESC LIMIT 10;   
                                    """
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    res = []
                    for i in result:
                        res.append(i)

                    return res


        except Exception as e:
            self.mistake = e