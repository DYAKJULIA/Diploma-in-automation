import allure
import pytest
from API.Clients.kinopoisk_client import KinopoiskClient
from Config.settings import Settings

@allure.feature("API тесты")
@allure.story("Поиск фильма с названием в несколько слов")
@pytest.mark.parametrize("title", ["Граф Монте-Кристо",
                                  "1+1",
                                  "Соломон Кейн"])
def test_search_movie_by_title_2_words(title):
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)
    response = client.search_movie_by_title(title)
    assert response["docs"][0]["name"] == title
