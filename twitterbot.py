from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from handle import mouse

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
        time.sleep(5)

    
    def logout(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        
        time.sleep(3)
        try:
            menuAccount_button = bot.find_element(By.XPATH, "(//div[@aria-label='Account menu'])[1]")
            menuAccount_button.click()
            time.sleep(2)
            bot.find_element(By.XPATH, "//span[starts-with(normalize-space(),'Log out @')]").click()
            time.sleep(2)
            bot.find_element(By.XPATH, "//span[@class='css-1qaijid r-bcqeeo r-qvutc0 r-poiln3'][normalize-space()='Log out']")
            time.sleep(3)

        except NoSuchElementException:
            print("Element not found. Skipping logout.")
            return
    
    def post_tweet(self, image_path):
        bot = self.bot
  
        time.sleep(2)
        
        text_box = bot.find_element(By.XPATH, "(//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr'])[1]")
        text_box.click()
        time.sleep(1)
        text_box.send_keys("Day la text duoc nhap tu bot")
        time.sleep(1)
        
        if image_path is not None:
            input_element = bot.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/nav/div/div[2]/div/div[1]/div/input")
            input_element.send_keys(image_path)
            print("upload image")
            time.sleep(5)
            
        post_button = bot.find_element(By.XPATH, "(//div[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19u6a5r r-2yi16 r-1qi8awa r-ymttw5 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l'])[1]")
        post_button.click()
        time.sleep(3)
        
        try:
            got_it_button = bot.find_element(By.XPATH, "//div[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1mnahxq r-19yznuf r-64el8z r-1dye5f7 r-1loqt21 r-o7ynqc r-6416eg r-oelmt8 r-1ny4l3l']//div[@class='css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci']")
            got_it_button.click()
            time.sleep(3)
        except NoSuchElementException:
            print("Skip got it")
         
        avatar_button = bot.find_element(By.XPATH, "(//div[@class='css-175oi2r r-12181gd r-1pi2tsx r-13qz1uu r-o7ynqc r-6416eg r-1ny4l3l'])[1]")
        avatar_button.click()
        time.sleep(2)
        scroll_height = bot.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
        scroll_increment = 5  

        for i in range(0, scroll_height, scroll_increment):
            bot.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.1) 
        
        # mouse.slow_scroll_and_close(self)
        
        time.sleep(3)
        bot.close()