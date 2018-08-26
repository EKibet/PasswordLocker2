import unittest
import sys
import User from user_data

class UserTestCases():

    def tearDown(self):
        User.users_list=[]

    def setUp(self):
        new_user = User("Edgar","pass123")

    def test_if_user_instance_returns_expected_output(self):
        
