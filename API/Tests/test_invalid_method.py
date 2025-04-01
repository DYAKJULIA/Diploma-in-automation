import allure
from API.Clients.kinopoisk_client import KinopoiskClient
from Config.settings import Settings


@allure.feature("API тесты")
@allure.story("Поиск с неправильным методом")
def test_search_movie_invalid_method():
    client = KinopoiskClient(base_url=Settings.KINOPOISK_API_URL, api_key=Settings.API_KEY)

    with allure.step("Используем неправильный метод для поиска"):
        response = client.search_movie_invalid_method()

    with allure.step("Проверка статус кода"):
        assert response.status_code == 404