from Pages.BaseClass import BaseClass
import time

class Post(BaseClass):

    def write_post(self, text, photo='yes'):
        post = self.driver.find_element_by_name("Post")
        post.click()

        write_post = self.driver.find_element_by_id("activity_post_story_edit_text")
        write_post.send_keys(text)

        if(photo=='yes'):
            self.__add_image()

    def __add_image(self, options='camera'):
        if(options=='camera'):
            add_image = self.driver.find_element_by_id("view_post_story_bar_camera")
            add_image.click()
            activity = self.driver.current_activity
            print("----------------------------------------------------------")
            print(activity)
            try:
                take_picture = self.driver.find_element_by_id("MENUID_SHUTTER") #5.1.1
                take_picture.click()
            except Exception as e:
                print("Error in taking the picture: ", e)

            activity = self.driver.current_activity
            print(activity)
            time.sleep(1)
            ok_button = self.driver.find_element_by_name("OK")
            ok_button.click()

        else:
            add_image = self.driver.find_element_by_id("view_post_story_bar_gallery")
            add_image.click()





