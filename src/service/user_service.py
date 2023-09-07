from repository.user_repository import UserRepository

userRepository = UserRepository()

class UserService:
    
    @staticmethod
    def list():

        data = {}
        users = userRepository.findAll()
        
        if users != None:
            for user in users:

                data[ user[0] ] = {
                    "name": user[1],
                    "username": user[2],
                    "email": user[3]
                }
            return data
        
        return {}
    
    @staticmethod
    def search(credential):
        
        user = userRepository.findByCredential(credential)
        if user != None:
            data = {
                "id": user[0],
                "name": user[1],
                "username": user[2],
                "email": user[3],
            }

            return data 
        
        return {}
    
    @staticmethod
    def add(user):
        return userRepository.save(user)