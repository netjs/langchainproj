import mysql.connector

class MySQLConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None or not cls._connection.is_connected():
            cls._connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="netjs"
            )
        return cls._connection