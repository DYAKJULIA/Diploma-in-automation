import allure
from UI.Pages.main import MainPage
from UI.Pages.search import KinopoiskSearchPage


@allure.feature("КИНОПОИСК")
class TestKinopoisk:
    @allure.story("Проверяем главную страницу")
    def test_main_page_title(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Закрыть модальное окно, если появилось"):
             search_page = KinopoiskSearchPage(driver)
             search_page.close_modal()

        with allure.step("Проверяем заголовок страницы"):
            assert "КИНОПОИСК. Онлайн кинотеатр. Фильмы сериалы мультфильмы и энциклопедия" in UI.Pages.main.get_page_title()

    @allure.story("Проверяем поиск фильма")
    def test_search_movie(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Закрыть модальное окно, если появилось"):
             search_page = KinopoiskSearchPage(driver)
             search_page.close_modal()

        with allure.step("Проверяем, что поле поиска отображается"):
            assert main_page.search_input_is_displayed()

        with allure.step("Ищем фильм 'Еретик'"):
            search_page = KinopoiskSearchPage(driver)
            search_page.search_for_movie("Еретик")

        with allure.step("Проверяем, что первый результат соответствует запросу"):
            assert "Еретик" in search_page.get_first_result_title()

    @allure.story("Проверка наличия элементов на главной странице")
    def test_main_page_elements(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Закрыть модальное окно, если появилось"):
                search_page = KinopoiskSearchPage(driver)
                search_page.close_modal()

        with allure.step("Проверяем наличие логотипа"):
            assert main_page.find_element(('xpath',
            '//a[contains(@class, "styles_root__dYidr") and contains(@class, "styles_logo___bcop")]')).is_displayed()

    @allure.story("Проверка перехода в раздел 'Фильмы'")
    def test_top_250_link(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Закрыть модальное окно, если появилось"):
                search_page = KinopoiskSearchPage(driver)
                search_page.close_modal()

        with allure.step("Кликаем на кнопку 'Фильмы'"):
            main_page.click(('css selector',
                             'a.styles_root__7mPJN.styles_lightThemeItem__BSbZW[href="/lists/categories/movies/1/"]'))

        with allure.step("Проверяем URL страницы 'Фильмы'"):
            expected_url = "https://www.kinopoisk.ru/lists/categories/movies/1/"
            actual_url = driver.current_url
            assert actual_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {actual_url}"

        return actual_url

    @allure.story("Проверка перехода в раздел 'Сериалы'")
    def test_series_link(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Закрыть модальное окно, если появилось"):
                search_page = KinopoiskSearchPage(driver)
                search_page.close_modal()

        with allure.step("Кликаем на ссылку 'Сериалы'"):
            main_page.click(('css selector',
                             'a.styles_root__7mPJN.styles_lightThemeItem__BSbZW[href="/lists/categories/movies/3/"]'))

        with allure.step("Проверяем URL страницы 'Сериалы'"):
            expected_url = "https://www.kinopoisk.ru/lists/categories/movies/3/"
            actual_url = driver.current_url
            assert actual_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {actual_url}"

        return actual_url
