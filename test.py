import unittest
import sys
from user_data import Users 

class UserTestCases(unittest.TestCase):

    def tearDown(self):
        Users.users_list=[]

    def setUp(self):
        self.new_user = Users("Edgar","pass123")

    def test_if_user_instance_returns_expected_output(self):
        self.new_user.save_user()
        self.assertEqual(len(Users.users_list),1)


if __name__ == '__main__':
    unittest.main()