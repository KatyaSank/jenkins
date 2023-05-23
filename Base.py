from selenium.webdriver.common.by import By


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        return self.driver.get(url)

    def maximize_window(self):
        return self.driver.maximize_window()

    def get_locator_by_xpath(self, selector):
        xpath = (By.XPATH, selector)
        return self.driver.find_element(*xpath)
