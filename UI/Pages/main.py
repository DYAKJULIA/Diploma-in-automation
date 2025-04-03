from UI.Pages.base import BasePage
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.kinopoisk.ru/"
        self.wait = WebDriverWait(driver, 15)

    def open_main_page(self):
        self.open(self.url)

    def get_page_title(self):
        return self.driver.title

    def search_input_is_displayed(self):
        return self.find_element(('name', 'kp_query')).is_displayed()
