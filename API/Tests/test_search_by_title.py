import allure
import pytest
from Config.settings import Settings
from API.Clients.kinopoisk_client import KinopoiskClient


@allure.feature("API тесты")
@allure.story("Поиск фильма по названию")
@pytest.mark.parametrize("title", ["Еретик",
                                  "Левша",
                                  "Дюна"])
def test_search_movie_by_title(title):
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)
    response = client.search_movie_by_title(title)
    assert response["docs"][0]["name"] == title
