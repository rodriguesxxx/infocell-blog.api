import mysql.connector
from mysql.connector import Error

class MysqlDb:
    def __init__(self):
        self.enginer = self.__create_conection()
        self.cursor = self.enginer.cursor() if self.enginer != None else None

    def __create_conection(self):
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="infocell_blog"
            )
        except Error as e:
            return None
        
    
        
    

    
