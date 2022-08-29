import config
import mysql.connector


class Report_development4:
    def __init__(self):
        self.mistake = ''

    def processing_report(self):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_profitability = f"""SELECT idFL,idL, SUM(payoutAmount) as money
                                        FROM insurancePolicyClient, payoutsDirectoryClient
                                        WHERE insurancePolicyClient.policyNumber = payoutsDirectoryClient.policyNumber
                                        GROUP BY idFL, idL order by money DESC LIMIT 10;  
                                    """
                with connection.cursor() as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    filename = 'report4_result.txt'
                    f = open(filename, 'w')
                    for i in result:
                        f.write(''.join(map(lambda a: str(a).ljust(22), i)) + '\n')


        except Exception as e:
            self.mistake = e