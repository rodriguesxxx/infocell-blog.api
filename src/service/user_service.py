from repository.user_repository import UserRepository

userRepository = UserRepository()

class UserService:
    
    @staticmethod
    def list():
        return userRepository.findAll()
    
    @staticmethod
    def add(user):
        return userRepository.save(user)