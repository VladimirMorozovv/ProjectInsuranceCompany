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
                with connection.cursor() as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    filename = 'report5_result.txt'
                    f = open(filename, 'w')
                    for i in result:
                        f.write(''.join(map(lambda a: str(a).ljust(22), i)) + '\n')


        except Exception as e:
            self.mistake = e