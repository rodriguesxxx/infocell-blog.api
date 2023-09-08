from database.mysql import MysqlDb

class UserRepository:
    def __init__(self):
        self.mysqlDb = MysqlDb()
        self.cnx = self.mysqlDb.enginer
        self.cursor = self.mysqlDb.cursor

          
    def save(self, user):
        
        try:
            query = "INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s)"
            values = (user.get_name(), user.get_username(), user.get_email(), user.get_password())
            self.cursor.execute(query, values)
            self.cnx.commit()
            return True
        
        except Exception as error:
            self.cnx.rollback()
            print(error)
            return False
        
    def delete(self, id):
        try:
            query = "DELETE FROM users WHERE id=%s"
            values = (id)
            self.cursor.execute(query, values)
            self.cnx.commit()
            return True
            
        except Exception as error:
            self.cnx.rollback()
            print(error)
            return False

    def findAll(self):
        try:
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            # self.cnx.commit()
            return self.cursor.fetchall()
        
        except Exception as error:
            self.cnx.rollback()
            print(error)
            return False

    def findByCredential(self, credential):
        try:
            
            query = "SELECT * FROM users WHERE username = %s OR email = %s"
            values = (credential, credential)
            self.cursor.execute(query, values)
            self.cnx.commit()
            return self.cursor.fetchone()
        
        except Exception as error:
            self.cnx.rollback()
            print(error)
            return False
  
    