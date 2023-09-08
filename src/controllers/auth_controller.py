from models.user import User
from service.user_service import UserService

userService = UserService()
class UserController:
    def __init__(self):
        pass

    def list(self):
        return userService.list()
    
    def search(self, credential):
        return userService.search(credential)

class RegisterController:

    def __init__(self, json_data):
        self.__user = User( json_data['name'], json_data['username'], json_data['email'], json_data['password'] )
        
    def register(self):
        return userService.add(self.__user)

class DeleteController:
    def __init__(self, id):
        self.id = id
    
    def delete(self):
        return  userService.delete(self.id)