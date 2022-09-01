import config
import mysql.connector

class Report_development6:
    def __init__(self):
        self.mistake = ''

    def profitability(self):

        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_profitability = """SELECT OUTPUT.sum - INPUT.sum AS 'Разница между проданными полисами и выплат
                                       страхователям' FROM (SELECT SUM(costInsurance) sum FROM insurancePolicyClient 
                                      WHERE status='sold') OUTPUT, (SELECT SUM(payoutAmount) sum 
                                      FROM payoutsDirectoryClient) INPUT"""
                with connection.cursor() as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    filename = 'report6_result.txt'
                    f = open(filename, 'w')
                    for i in result:
                        f.write(''.join(map(lambda a: str(a).ljust(22), i)) + '\n')

        except Exception as e:
            self.mistake = e




