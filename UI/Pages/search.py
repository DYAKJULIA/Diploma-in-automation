from UI.Pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KinopoiskSearchPage(BasePage):
    SEARCH_FIELD = (By.NAME, "kp_query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    SEARCH_RESULTS = (By.CLASS_NAME, "search-results")
    CLOSE_MODAL = (By.CSS_SELECTOR, "[data-tid='d6ef5dc']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_search_page(self):
        self.driver.get("https://www.kinopoisk.ru/")

    def close_modal(self):
        self.wait.until(
        EC.element_to_be_clickable(self.CLOSE_MODAL)
        ).click()


    def search_movie_by_phrase(self, title):
        self.send_keys(self.SEARCH_FIELD, title)
        self.click(self.SEARCH_BUTTON)


    def get_search_results(self):
        return self.is_visible(self.SEARCH_RESULTS)

    def search_for_movie(self, movie_name):
        self.send_keys(('name', 'kp_query'), movie_name)
        self.click(('xpath', '//button[@type="submit"]'))


    def get_first_result_title(self):
        #return self.find_element(('xpath', '//div[@class="element most_wanted"]//a[@class="name"]')).text
        return self.find_element(
            ('css selector', "div[class='element most_wanted'] div[class='info'] a[class='js-serp-metrika']")).text
