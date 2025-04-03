from UI.Pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KinopoiskAutorizationPage(BasePage):
    # Поле ввода для номера телефона
    PHONE_INPUT = (By.XPATH, "//input[@id='passp-field-phone']")
    # Кнопка войти и "Отправить код"
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='passp:sign-in']")
    # Поле ввода для кода из push-уведомления
    CODE_INPUT = (By.XPATH, "//input[@id='passp-field-phoneCode']")
    PROFILE_SELECTION = (By.CSS_SELECTOR, ".AccountsListItem-login")  # Выбор аккаунта
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'styles_loginButton__LWZQp') and text()='Войти']")   # Кнопка 'Войти'
    CLOSE_MODAL = (By.CSS_SELECTOR,"[data-tid='d6ef5dc']")
    AVATAR_PIC = (By.CSS_SELECTOR,"[data-tid='15bd9013']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_page_autorization(self):
        self.driver.get("https://www.kinopoisk.ru/")

    def close_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CLOSE_MODAL)
        ).click()

    def click_login_button(self):
        """Нажатие кнопки 'Войти'."""
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def enter_phone_number(self, phone_number):
        """
        Ввод номера телефона.

        :param phone_number: Номер телефона для входа.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.PHONE_INPUT)
        ).send_keys(phone_number)

    def submit_phone_number(self):
        """Нажатие кнопки 'Войти'."""
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()


    def select_profile(self, profile_name):
        """
        Выбор аккаунта
        """
        self.wait.until(
            EC.element_to_be_clickable(self.PROFILE_SELECTION)
        ).click()

    def authorization_check(self):
        """Проверка, что пользователь авторизован."""
        try:
            self.wait.until(EC.presence_of_element_located(self.AVATAR_PIC))
            return True
        except:
            return False
