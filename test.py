import unittest
import sys
from user_data import Users 
from credentials import Credentials

class UserTestCases(unittest.TestCase):

    def tearDown(self):
        Users.users_list=[]
        '''
        clears the users list before next method
        '''

    def setUp(self):
        '''
        python will run this instruction every time
        it encounters a new method
        '''
        self.new_user = Users("Edgar","pass123")
        self.new_credential = Credentials("facebook", "ekibe", "pass123")
    def test_if_user_can_create_an_account(self):

        '''
        tests if created user account is saved
        in the list
        '''

        self.new_user.save_user()
        self.assertEqual(len(Users.users_list),1)
    def test_user_with_an_account_can_login(self):
        
        '''
        test to check if a user exists
        '''
        self.new_user.save_user()
        user_exist  = Users.find_by_username("Edgar")
        self.assertTrue(user_exist)  

    def test_user_with_an_account_can_login(self):
        
        '''
        tests if user can log in using the credentials already saved 
        in users list
        '''
        self.new_user.save_user()
        validate_user = Users.check_user("Edgar","pass123")
        self.assertEqual(validate_user, self.new_user.user_name)
    
    # Tests credentials
    def test_if_user_can_create_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()

    