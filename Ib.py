from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
         driver = self.driver
         driver.get('https://www.instagram.com/accounts/login/')
         time.sleep(2)
         user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
         user_name_elem.clear()
         user_name_elem.send_keys(self.username)
         password_elem = driver.find_element_by_xpath("//input[@name='password']")
         password_elem.clear()
         password_elem.send_keys(self.password)
         password_elem.send_keys(Keys.RETURN)
         time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range (1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)


        # searching for picrie link

        hrefs = driver.find_elements_by_tag_name('a')
        post_tag = '/p/'
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]

        pic_hrefs =  [href for href in pic_hrefs if post_tag in href]
        print(pic_hrefs)
        print(hashtag + 'photos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_css_selector('.dCJp8').click()
                time.sleep(20)
            except Exception as e:
                time.sleep(4)

silkyIG = InstagramBot("xxxxx", "xxxxxx") # Add Account and Password
silkyIG.login()
silkyIG.like_photo('Photo to start liking') # Photo to like

hashtags = ['instaostkanten'] # Add hashtag

[silkyIG.like_photo(tag) for tag in hashtags]
