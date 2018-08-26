import sys

class Users():
    users_list=[]
    def __init__(self,user_name,user_password):
        self.user_name = user_name
        self.user_password = user_password
    

    def save_user(self):
        if self.user_name != " " and self.user_password != " ":
            Users.users_list.append(self)
        else:
            print("username or password given is empty")
    
    @classmethod
    def find_by_username(cls,username):
        '''
        searchs for a specific user using
        value passed at username arg 
        '''
        for user in cls.users_list:
            if user.user_name == username:
                return True
            return False

    @classmethod
    def check_user(cls,username,password):
        '''
        checks if the name and password entered matchs
        '''
        current_user = ""
        for user in cls.users_list:
            if user.user_name == username and user.user_password == password:
                current_user = user.user_name
                return current_user
