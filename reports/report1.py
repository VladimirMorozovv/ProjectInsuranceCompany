import config
import mysql.connector

class Report_development1:
    def __init__(self, data_start, data_stop):
        self.data_start = data_start
        self.data_stop = data_stop
        self.mistake = ""

    def processing_report(self, data_start, data_stop):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_profitability = f"""SELECT typesInsuranceObjects.ObjectType, SUM(insurancePolicyClient.costInsurance)
                                        FROM typesInsuranceObjects, insurancePolicyClient
                                        WHERE insurancePolicyClient.idTypeObject = typesInsuranceObjects.idTypes 
                                        and insurancePolicyClient.startDate BETWEEN '{data_start}' and '{data_stop}'
                                        GROUP BY typesInsuranceObjects.ObjectType;"""
                with connection.cursor() as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    filename = 'report1_result.txt'
                    f = open(filename, 'w')
                    for i in result:
                        f.write(''.join(map(lambda a: str(a).ljust(22), i)) + '\n')


        except Exception as e:
            self.mistake = e
