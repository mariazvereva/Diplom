import pytest
from pages.registration import Registr
from selenium.webdriver.common.by import By
from pages.locators import Registration


def test_registration_with_valid_data(selenium):
   '''Тест ТС-020. Проверяем, что новый  пользователь может успешно зарегистрироваться с корректными данными'''
   #проверяю регистрацию только до проверочного кода, так как указанная электронная почта в реальности не существует

   page = Registr(selenium)
   page.driver.find_element(By.ID, 'kc-register').click()

   page.driver.find_element(*Registration.NAME).send_keys("Мария")
   page.driver.find_element(*Registration.SURNAME).send_keys("Мария")

   page.driver.implicitly_wait(10)

   page.driver.find_element(*Registration.MAIL_OR_PHONE).send_keys('123456789fghcn@mail.ru')
   page.driver.implicitly_wait(10)
   page.driver.find_element(*Registration.PASSWORD).send_keys('123456789Pa')
   page.driver.find_element(*Registration.PASSWORD_CONFIRM).send_keys('123456789Pa')
   page.driver.implicitly_wait(10)
   page.driver.find_element(*Registration.BTN_REGISTR).click()

   assert page.driver.find_element(By.ID, "rt-code-0")

def test_registration_with_registered_data(selenium):
   '''Тест ТС-021. Попытка регистрации пользователя по уже зарегистрированному в системе номеру телефона'''


   page = Registr(selenium)
   page.driver.find_element(By.ID, 'kc-register').click()

   page.driver.find_element(*Registration.NAME).send_keys("Мария")
   page.driver.find_element(*Registration.SURNAME).send_keys("Мария")

   page.driver.implicitly_wait(10)

   page.driver.find_element(*Registration.MAIL_OR_PHONE).send_keys('+79210664745')
   page.driver.implicitly_wait(10)
   page.driver.find_element(*Registration.PASSWORD).send_keys('123456789Pa')
   page.driver.find_element(*Registration.PASSWORD_CONFIRM).send_keys('123456789Pa')
   page.driver.implicitly_wait(10)
   page.driver.find_element(*Registration.BTN_REGISTR).click()

   assert page.driver.find_element(By.CLASS_NAME, "card-modal__title").text == "Учётная запись уже существует"


def generate_string(n): #вспомогательная функция для генерации строки с требуемым количеством символов
   return "x" * n
@pytest.mark.parametrize('data', ["abcdefgh",
                                        "№$#!@*",
                                        'a',
                                        ""
                                        "123456789",
                                        generate_string(255),
                                        generate_string(1001)])

def test_name_field_negativ(selenium, data):
   '''Тест ТС-022. Проверка поля "Имя" при регистрации нового пользователя на ввод некоррекных данных '''


   page = Registr(selenium)
   page.driver.find_element(By.ID, 'kc-register').click()

   page.driver.find_element(*Registration.NAME).send_keys(data+'\n')

   page.driver.implicitly_wait(10)


   assert page.driver.find_element(By.CLASS_NAME, "rt-input-container__meta--error").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

@pytest.mark.parametrize('data', ["abcdefgh",
                                        "№$#!@*",
                                        'a',
                                        ""
                                        "123456789",
                                        generate_string(255),
                                        generate_string(1001)])
def test_surname_field_negativ(selenium, data):
   '''Тест ТС-023. Проверка поля "Фамилия" при регистрации нового пользователя на ввод некоррекных данных '''


   page = Registr(selenium)
   page.driver.find_element(By.ID, 'kc-register').click()

   page.driver.find_element(*Registration.SURNAME).send_keys(data+'\n')

   page.driver.implicitly_wait(10)


   assert page.driver.find_element(By.CLASS_NAME, "rt-input-container__meta--error").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


@pytest.mark.parametrize('data', ["12345абв", "12345678" , "12345abc", "12345ABC", "123", "abcdefge"
                                        "№$#!@*", "", generate_string(255), generate_string(1001)])
def test_password_field_negativ(selenium, data):
   '''Тест 024.Проверка поля "Пароль" при регистрации нового пользователя на ввод некоррекных данных '''


   page = Registr(selenium)
   page.driver.find_element(By.ID, 'kc-register').click()

   page.driver.find_element(*Registration.PASSWORD).send_keys(data+'\n')

   page.driver.implicitly_wait(10)


   assert page.driver.find_element(By.CLASS_NAME, "rt-input-container__meta--error").text == \
          "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру" \
          or "Длина пароля должна быть не менее 8 символов" or "Пароль должен содержать хотя бы одну заглавную букву" \
          or "Пароль должен содержать хотя бы одну строчную букву" or "Пароль должен содержать только латинские буквы"

