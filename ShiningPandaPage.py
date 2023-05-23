from Base import *


class Panda(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://plugins.jenkins.io/shiningpanda/"
        self.panda_locator = "//h1[@class='title']"
        self.text = 'ShiningPanda'

    def open_url(self):
        return self.get_url(self.url)

    def assert_panda_title_by_text(self):
        assert self.get_locator_by_xpath("//h1[@class='title']").text == "ShiningPanda"
