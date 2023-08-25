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
            return False
    def save(self, user):
        
        try:
            query = f"INSERT INTO users(name, username, email, password) VALUES({user.get_name()}, {user.get_username()}, {user.get_email()}, {user.get_password()})"
            self.cursor.execute(query)
            return True
        except BaseException:
            return True