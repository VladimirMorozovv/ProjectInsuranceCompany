import mysql.connector
import config

try:
    with mysql.connector.connect(host=config.host,
                                 user=config.user,
                                 password=config.password,
                                 database=config.database,
                                 ) as connection:
        show_db_query = "show create table ClientFL"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for row in cursor:
                print(row)
except Exception as e:
    print(e)
    print('Не удалось подключится к базе')
