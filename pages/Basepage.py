from selenium.webdriver.common.by import By

class BasePage :
    def __int__(self,driver):
        self.driver = driver
        print("BasePage initialized")

    def open_url(self, url):
        self.driver.get(url)

    def send_keys_fun(self,Locator,value):
        self.driver.find_element(By.NAME, Locator).send_keys(value)

