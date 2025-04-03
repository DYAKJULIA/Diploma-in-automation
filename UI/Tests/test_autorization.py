import allure
from Config.settings import Settings
from UI.Pages.authorization import KinopoiskAutorizationPage


@allure.feature("UI Тесты")
@allure.story("Авторизация на сервисе 'КИНОПОИСК'")
def test_authorization(driver):
    login_page = KinopoiskAutorizationPage(driver)

    with allure.step("Открыть страницу входа"):
        login_page.open_page_autorization()

    with allure.step("Закрыть модальное окно, если появилось"):
        login_page.close_modal()

    with allure.step("Нажать кнопку 'Войти'"):
        login_page.click_login_button()

    with allure.step("+7(999) 000-99-00"): # Ввести свой номер телефона
        login_page.enter_phone_number(Settings.USER_PHONE)

    with allure.step("Нажать кнопку 'Войти'"):
        login_page.submit_phone_number()

    with allure.step("Выбрать профиль 'Мой профиль'"):
        login_page.select_profile("Мой профиль")

    with allure.step("Проверить, что пользователь авторизован"):
        assert login_page.authorization_check(), "Пользователь не авторизован"
