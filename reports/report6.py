import config
import mysql.connector


class Profitability:
    def __init__(self):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_movies_query = "SELECT OUTPUT.sum - INPUT.sum AS 'Разница между проданными полисами и выплат" \
                                      " страхователям' FROM (SELECT SUM(costInsurance) sum FROM insurancePolicyClient " \
                                      "WHERE status='sold') OUTPUT, (SELECT SUM(payoutAmount) sum " \
                                      "FROM payoutsDirectoryClient) INPUT"
                with connection.cursor() as cursor:
                    cursor.execute(select_movies_query)
                    result = cursor.fetchall()
                    for row in result:
                        self.result = row

        except Exception as e:
            self.mistake = e




    def profitability(self, difference):
        if difference >= 0:
            return f'Прибыль компании составляет {difference}'
        elif difference < 0:
            return f'Убыток компании составляет {difference}'