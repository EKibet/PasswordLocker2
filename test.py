import unittest
import sys
from user_data import Users 

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
        self.asserTrue(user_exist)  

    # def test_user_with_an_account_can_login(self):
        
    #     '''
    #     tests if user can log in using the credentials already saved 
    #     in users list
    #     '''
    #     self.new_user.save_user
    #     self.asserTrue()

if __name__ == '__main__':
    unittest.main()