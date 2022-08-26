import config
import data_object_type
import mysql.connector


class Managing_object_type:

    def add(self, object_type: data_object_type.ObjectType):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_object_type = f"""
                    INSERT INTO typesInsuranceObjects
                    (ObjectType)
                    VALUES
                    ({object_type.ObjectType});

                """
                with connection.cursor() as cursor:
                    cursor.execute(add_object_type)
                    connection.commit()
        except Exception as e:
            return e

    def change(self, object_type: data_object_type.ObjectType):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_object_type = f"""
                    UPDATE typesInsuranceObjects SET ObjectType = {object_type.ObjectType} WHERE idTypes = {object_type.idTypes};
                """
                with connection.cursor() as cursor:
                    cursor.execute(change_object_type)
                    connection.commit()
        except Exception as e:
            return e

    def delete(self, object_type: data_object_type.ObjectType):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_object_type = f"""
                    DELETE FROM objectsInsurance
                    WHERE idObjects={object_type.idTypes}
                """
                with connection.cursor() as cursor:
                    cursor.execute(delete_object_type)
                    connection.commit()
        except Exception as e:
            return e