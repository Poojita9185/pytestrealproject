import pytest


@pytest.mark.usefixtures("launch_browser")
class BaseFile:
    pass
    # def object_creation(self):
    #     self.homepage=HomePage(self.driver)
