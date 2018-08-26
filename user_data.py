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
        for user in cls.users_list:
            if user.user_name == username:
                return True
            return False


