from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


import time
import os


class TwitterBot:

    def __init__(self, email, password):
        self.email = email
        self.password = password

        chrome_options = Options()
        chrome_options.add_argument("executable_path=" + os.path.join(os.getcwd(), 'driver'))

        self.bot = webdriver.Chrome(options=chrome_options)

    def login(self):

        bot = self.bot
        bot.get("https://twitter.com/login")

        time.sleep(3)
        print(self.email)
        print(self.password)
        
        email = bot.find_element(By.XPATH , "//input[@name='text']")
        email.send_keys(self.email)
        next_button = bot.find_element(By.XPATH, "(//div[@class='css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci'])[3]")
        next_button.click()
        time.sleep(3)
        
        password = bot.find_element(By.XPATH ,"//input[@name='password']")
        password.send_keys(self.password)
        login_button = bot.find_element(By.XPATH, "(//div[@class='css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci'])[3]")
        login_button.click()
        time.sleep(10)

        