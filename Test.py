from Pages.SignUpPage import SignIn
from BaseTest import  BaseTest
import unittest

class MyTestCase(BaseTest):

    def test_login(self):
        sign_in = SignIn(self.driver)
        sign_in.sign_up_button()
        user_1 = sign_in.login()
        user_1.write_post("New Post")



if __name__ == '__main__':
    unittest.main()














