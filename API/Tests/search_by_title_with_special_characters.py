import allure
import pytest
from API.Clients.kinopoisk_client import KinopoiskClient
from Config.settings import Settings

@allure.feature("API тесты")
@allure.story("Поиск фильма с спецсимволами в названии")
@pytest.mark.parametrize("title", ["%()",
                                  "----",
                                  "><//"])
def search_by_title_with_special_characters(title):
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)
    response = client.search_movie_by_title(title)
    assert response["docs"][0]["name"] == title

    with allure.step("Проверка статус кода"):
        assert response.status_code == 400