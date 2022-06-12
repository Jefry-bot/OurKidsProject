import pymysql

class DataBase:
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host = 'localhost', 
            user = 'root',
            password = '',
            db = 'springboot',
            port= 3306
        )

        self.cursor = self.connection.cursor()

    def commit(self) -> None:
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()