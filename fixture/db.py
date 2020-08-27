import mysql.connector

from model.group import Group


class DbFixture:
    def __init__(self, host, port, db_name, user, password):
        self.port = port
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, port=port, database=db_name,
                                                  user=user, password=password, autocommit=True)

    def get_group_list(self):
        list_group = []
        with self.connection.cursor() as cur:
            cur.execute("SELECT group_id, group_name, group_header, group_footer "
                        "FROM group_list "
                        "WHERE deprecated = '0000-00-00 00:00:00'")
            for row in cur:
                (id, name, header, footer) = row
                list_group.append(Group(id=str(id), name=name, header=header, footer=footer))
        return list_group

    def destroy(self):
        self.connection.close()
