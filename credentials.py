import sys


class Credentials():
    credentials_list = []
    def __init__(self,site_name,site_username,site_password):
        self.site_name = site_name
        self.site_username = site_username
        self.site_password = site_password

    def save_credential(self):
        user_data = {
            site_name
        }
        self.credentials_list.push(self)

    
    @classmethod
    def display_credentials(cls):
        for credential in cls.credentials_list:
            return credential

    @classmethod
    def find_by_sitename(cls,search):
        for credentials in cls.credentials_list:
            if credentials.site_name == search:
                return credentials
