import config
import mysql.connector

class Report_development3:
    def __init__(self, id):
        self.id = id
        self.mistake = ""


    def processing_report(self, id):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_profitability = f"""SELECT policyNumber, stopDate FROM insurancePolicyClient
                                        WHERE idL={id} and stopDate > CURRENT_DATE();  
                                    """
                with connection.cursor() as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    filename = 'report3_result.txt'
                    f = open(filename, 'w')
                    for i in result:
                        f.write(''.join(map(lambda a: str(a).ljust(22), i)) + '\n')


        except Exception as e:
            self.mistake = e