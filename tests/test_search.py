import allure

from pages.Homepage import HomePage
from tests.test_basefile import BaseFile


class TestSearch(BaseFile):

    @allure.description("Searching product")
    @allure.id("id123")
    def test_search_product(self):
        homepage = HomePage(self.driver)
        homepage.go_to_home_page()
        homepage.enter_product_into_search("HP")

    @allure.severity("High")
    @allure.story("GSCE")
    def test_click_product(self):
        homepage = HomePage(self.driver)
        homepage.click_product()
