import mysql.connector


class DbFixture:
    def __init__(self, host, port, db_name, user, password):
        self.port = port
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, port=port, database=db_name,
                                                  user=user, password=password)

    def destroy(self):
        self.connection.close()
