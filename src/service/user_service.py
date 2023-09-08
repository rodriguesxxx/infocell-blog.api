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
        
        return None
    
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
        
        return None
    
    @staticmethod
    def add(user):
        
        if( UserService.search( user.get_email() ) == None):
            if( UserService.search( user.get_name() ) == None ):
                return userRepository.save(user)   
            
            return "The username is already registered"
        return "The email is already registered"

    @staticmethod
    def delete(id):
        return userRepository.delete(id)

