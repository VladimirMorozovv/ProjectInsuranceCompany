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
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    print(result)
                    res = []
                    for i in result:
                        res.append(i)

                    return res


        except Exception as e:
            self.mistake = e