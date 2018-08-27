import sys
import pyperclip

class Credentials():
    credentials_list = []
    def __init__(self,site_name,site_username,site_password):
        self.site_name = site_name
        self.site_username = site_username
        self.site_password = site_password

    def save_credential(self):
        
        self.credentials_list.append(self)

    
    @classmethod
    def display_credentials(cls):
        for credential in cls.credentials_list:
            return credential

    @classmethod
    def find_by_sitename(cls,search):
        for credentials in cls.credentials_list:
            if credentials.site_name == search:
                return credentials
                
    @classmethod
    def copy_credential(cls,site_name):
        '''
        Class method that copies a credential's info after the credential's site name is entered
        '''
        found_credential = cls.find_by_sitename(site_name)
        return pyperclip.copy(found_credential.site_password)