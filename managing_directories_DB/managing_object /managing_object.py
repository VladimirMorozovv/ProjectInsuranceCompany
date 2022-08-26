import config
import data_object
import mysql.connector


class Managing_object:

    def add(self, object: data_object.Object):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_object = f"""
                    INSERT INTO objectsInsurance
                    (Name, numberPassport, idTypeObject)
                    VALUES
                    ('{object.Name}', '{object.numberPassport}', {object.idTypeObject})

                """
                with connection.cursor() as cursor:
                    cursor.execute(add_object)
                    connection.commit()
        except Exception as e:
            return e

    def change(self, object: data_object.Object):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_object = f"""
                    UPDATE objectsInsurance SET Name = '{object.Name}', numberPassport = '{object.numberPassport}', idTypeObject ={object.idTypeObject}
                    WHERE id = {object.idObjects}
                """
                with connection.cursor() as cursor:
                    cursor.execute(change_object)
                    connection.commit()
        except Exception as e:
            return e

    def delete(self, object: data_object.Object):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_object = f"""
                    DELETE FROM objectsInsurance
                    WHERE idObjects={object.idObjects}
                """
                with connection.cursor() as cursor:
                    cursor.execute(delete_object)
                    connection.commit()
        except Exception as e:
            return e