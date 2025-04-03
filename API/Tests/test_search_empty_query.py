import allure
import pytest
from Config.settings import Settings
from API.Clients.kinopoisk_client import KinopoiskClient


@allure.feature("API тесты")
@allure.story("Поиск с пустым значением query (обязательный параметр)")
@pytest.mark.xfail
def test_search_movie_empty_query():
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Поиск фильм с пустым запросом"):
        response = client.search_movie_empty_query()

    with allure.step("Проверка статус кода"):
        assert response.status_code == 400
