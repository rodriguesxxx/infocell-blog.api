from database.mysql import MysqlDb

class UserRepository:
    def __init__(self):
        self.mysqlDb = MysqlDb()
        self.cursor = self.mysqlDb.cursor

    def findAll(self):
        try:
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except BaseException:
            return "error"