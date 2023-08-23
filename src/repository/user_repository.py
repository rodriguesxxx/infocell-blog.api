import mysql.connector
from mysql.connector import Error

class UserRepository:
    def __init__(self):
        self.enginer = self.__create_conection

    def __create_conection():
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="blog_infocell"
            )
        except Error as e:
            return None
    

    
user = UserRepository()
print(user.enginer)