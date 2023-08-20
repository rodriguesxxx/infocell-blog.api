from models.user import User

class RegisterController:

    def __init__(self, json_data):
        self.__user = User( json_data['name'], json_data['username'], json_data['email'], json_data['password'] )
        
    def register(self):
        pass
