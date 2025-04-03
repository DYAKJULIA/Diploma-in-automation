import allure
from Config.settings import Settings
from API.Clients.kinopoisk_client import KinopoiskClient


@allure.feature("API тесты")
@allure.story("Поиск фильма по ID")
def test_search_movie_by_id():
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)
    response = client.search_movie_by_id(5942378)
    assert response["name"] == "Еретик"
