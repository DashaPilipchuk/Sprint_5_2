from selenium.webdriver.common.by import By


class Locators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    REGISTRATION_TO_ACCOUNT_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    INVALID_PASSWORD_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    ENTER = (By.XPATH, "//h2[text()='Вход']")
    REGISTRATION = (By.XPATH, "//h2[text()='Регистрация']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']")
    RECOVER_THE_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")
    RECOVER_THE_PASSWORD = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()= 'Личный Кабинет']")
    PERSONAL_ACCOUNT_TEXT = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()= 'Конструктор']")
    BURGER_TEXT = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    ROLLS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
    SAUCES = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')
    FILLINGS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')






