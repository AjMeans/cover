from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

import config


class Driver(object):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_LOCAL_PATH,
                                       chrome_options=options)
        self.username = config.LOGIN_USER
        self.password = config.LOGIN_PASS

    def login(self, login_url):
        self.driver.get(login_url)

        wait = WebDriverWait(self.driver, 5)
        userid = wait.until(EC.visibility_of_element_located((By.ID, "userid")))
        password = wait.until(EC.visibility_of_element_located((By.ID, "password")))

        userid.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)


