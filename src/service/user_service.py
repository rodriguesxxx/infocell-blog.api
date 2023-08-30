from repository.user_repository import UserRepository

userRepository = UserRepository()

class UserService:
    
    @staticmethod
    def list():
        
        return str(userRepository.findAll())
    
    @staticmethod
    def add(user):
        return userRepository.save(user)