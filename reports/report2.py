import config
import mysql.connector

class Report_development2:
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
                select_profitability = f"""SELECT  SUM(payoutAmount) as SUM
                                        FROM payoutsDirectoryClient
                                        WHERE paymentDate BETWEEN '{data_start}' and '{data_stop}'; 
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