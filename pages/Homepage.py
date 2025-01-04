import time

from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    url= "https://tutorialsninja.com/demo/"
    search_box_feild = "search"

    def go_to_home_page(self):
        self.driver.get(self.url)

    def enter_product_into_search(self,product):
        self.driver.find_element(By.NAME, self.search_box_feild).send_keys(product)
        #self.send_keys_fun(self.search_box_feild , product)
        time.sleep(5)

    def click_product(self):
        self.driver.find_element(By.XPATH , "//a[text()='Tablet123']").click()
        time.sleep(5)

