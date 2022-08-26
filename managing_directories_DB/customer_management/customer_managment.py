import config
import data_clients
import mysql.connector


class CustomerFL_managment:

    def add(self, client: data_clients.ClientFL):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_cleintsFL = f"""
                    INSERT INTO ClientFL
                    (FIO, residentialAddress, numberPassport, numberPhone)
                    VALUES
                    ({client.FIO}, {client.residentialAddress}, {client.numberPassport}, {client.numberPhone})

                """
                with connection.cursor() as cursor:
                    cursor.execute(add_cleintsFL)
                    connection.commit()
        except Exception as e:
            return e

    def change(self, client: data_clients.ClientFL):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_cleintsFL = f"""
                    UPDATE ClientFL SET
                    FIO = {client.FIO}, residentialAddress = {client.residentialAddress}, numberPassport={client.numberPassport}, numberPhone = {client.numberPhone}
                    WHERE id = {client.id}
                """
                with connection.cursor() as cursor:
                    cursor.execute(change_cleintsFL)
                    connection.commit()
        except Exception as e:
            return e

    def delete(self, client: data_clients.ClientFL):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_cleintsFL = f"""
                    DELETE FROM ClientFL
                    WHERE id = {client.id}
                """
                with connection.cursor() as cursor:
                    cursor.execute(delete_cleintsFL)
                    connection.commit()
        except Exception as e:
            return e


class CustomerL_managment:
    def add(self, client: data_clients.ClientL):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_cleintsL = f"""
                    INSERT INTO ClientLegal
                    (Name, legalAddress, OGRN, numberPhone)
                    VALUES
                    ({client.Name}, {client.legalAddress}, {client.OGRN}, {client.numberPhone})

                """
                with connection.cursor() as cursor:
                    cursor.execute(add_cleintsL)
                    connection.commit()
        except Exception as e:
            return e

    def change(self, client: data_clients.ClientL):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_cleintsFL = f"""
                    UPDATE ClientLegal SET
                    Name = {client.Name}, legalAddress = {client.legalAddress}, OGRN = {client.OGRN}, numberPhone = {client.numberPhone}
                    WHERE id = {client.id}
                """
                with connection.cursor() as cursor:
                    cursor.execute(change_cleintsFL)
                    connection.commit()
        except Exception as e:
            return e

    def delete(self, client: data_clients.ClientL):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_cleintsL = f"""
                    DELETE FROM ClientLegal
                    WHERE id = {client.id}
                """
                with connection.cursor() as cursor:
                    cursor.execute(delete_cleintsL)
                    connection.commit()
        except Exception as e:
            return e
