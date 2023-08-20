class User:
    def __init__(self, name, username, email, password):
        self.set_name(name)
        self.set_username(username)
        self.set_email(email)
        self.set_password(password)

    def get_name(self):
        return self.__name

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name):
        self.__name = name

    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    
    