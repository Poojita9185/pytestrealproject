
from pages.Homepage import HomePage
from tests.test_basefile import BaseFile


class TestSearch(BaseFile):

    def test_search_product(self):
        homepage = HomePage(self.driver)
        homepage.go_to_home_page()
        homepage.enter_product_into_search("HP")

    def test_click_product(self):
        homepage = HomePage(self.driver)
        homepage.click_product()
