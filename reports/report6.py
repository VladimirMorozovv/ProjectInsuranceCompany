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
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    res = []
                    for i in result:
                        res.append(i)

                    return res

        except Exception as e:
            self.mistake = e




