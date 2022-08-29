import config
import mysql.connector


class Viewing_development1:
    def __init__(self, date):
        self.date = date
        self.mistake = ''

    def processing_viewing(self, date):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_profitability = f"""SELECT * FROM insurancePolicyClient
                                        WHERE  stopDate = '{date} 00:00:00'  
                                    """
                with connection.cursor() as cursor:
                    cursor.execute(select_profitability)
                    result = cursor.fetchall()
                    filename = 'viewing1_result.txt'
                    f = open(filename, 'w')
                    for i in result:
                        f.write(''.join(map(lambda a: str(a).ljust(22), i)) + '\n')


        except Exception as e:
            self.mistake = e