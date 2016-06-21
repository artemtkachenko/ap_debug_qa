from Pages.BaseClass import BaseClass
from Pages.PostPage import Post

class SignIn(BaseClass):

    def sign_up_button(self):
        already_have_account = self.driver.find_element_by_id("activity_signup_already_have_account")
        already_have_account.click()

    def login(self):
        email = self.driver.find_element_by_id("activity_login_login_text_view")
        email.send_keys("pok")

        password = self.driver.find_element_by_id("activity_login_password_text_view")
        password.send_keys("qwertypok")

        continue_button = self.driver.find_element_by_id("activity_login_continue")
        continue_button.click()

        return Post(self.driver)

