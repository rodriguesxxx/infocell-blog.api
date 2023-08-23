from models.user import User
from service.user_service import UserService

class UserController:
    def __init__(self):
        self.userService = UserService()

    def showUsers(self):
        return self.userService.list()

class RegisterController:

    def __init__(self, json_data):
        self.__user = User( json_data['name'], json_data['username'], json_data['email'], json_data['password'] )
        
    def register(self):
        pass
