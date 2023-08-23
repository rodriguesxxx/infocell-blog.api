from repository.user_repository import UserRepository

userRepository = UserRepository()

class UserService:
    
    @staticmethod
    def list():
        return userRepository.findAll()