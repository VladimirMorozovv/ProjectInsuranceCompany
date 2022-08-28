import config
import mysql.connector

class :
    def __init__(self, data_start, data_stop):
        self.data_start = data_start
        self.data_stop = data_stop

    def processing_report(self, object_type: data_object_type.ObjectType):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_profitability = "SELECT OUTPUT.sum - INPUT.sum AS 'Разница между проданными полисами и выплат" \
                                       " страхователям' FROM (SELECT SUM(costInsurance) sum FROM insurancePolicyClient " \
                                       "WHERE status='sold') OUTPUT, (SELECT SUM(payoutAmount) sum " \
                                       "FROM payoutsDirectoryClient) INPUT"
                with connection.cursor() as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    for row in result:
                        self.result = row

        except Exception as e:
            self.mistake = e
