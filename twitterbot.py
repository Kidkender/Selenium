from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


import time
import os


class TwitterBot:

    def __init__(self, email, password):
        self.email = email
        self.password = password

        chrome_options = Options()

        self.bot = webdriver.Chrome(
            excutable_path=os.path.join(os.getcwd(), "/driver"),
            options=chrome_options
        )

    def login(self):

        bot = self.bot
        bot.get("https://twitter.com/login")

        time.sleep(3)

        email = bot.find_element_by_xpath(
            '//*[@id ="react-root"]/div / div / div[2]/main / div / div / form / div / div[1]/label / div / div[2]/div / input'
        )
        password = bot.find_element_by_xpath(
            '//*[@id ="react-root"]/div / div / div[2]/main / div / div / form / div / div[2]/label / div / div[2]/div / input'
        )

        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        time.sleep(2)
