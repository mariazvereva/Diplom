import pytest
from pages.auth_page import AuthPage, AuthPageCode
from settings import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep




@pytest.mark.parametrize('data', [valid_phone, valid_email])
def test_authorization_with_valid_data(selenium, data):
   '''Тест ТС-001. Проверяем, что зарегистрированный в системе пользователь может успешно
   авторизаваться с указанием корректного номера телефона/электронной почты и пароля
   (тестирование авторизации с использованием логина и лицевого счета не производится
    по причине отсутсвия валидных тестовых данных)'''

   page = AuthPage(selenium)
   page.enter_auth_field(data)
   page.driver.implicitly_wait(10)
   page.enter_pass(valid_pass)
   page.driver.implicitly_wait(10)
   page.btn_click()
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.ID, "lk-btn")


@pytest.mark.parametrize('data', [valid_phone, valid_email, "incorrect login"])
def test_authorization_with_incorrect_data(selenium, data):
   '''Тест ТС-002. Проверяем, что при вводе некорректного пароля не произойдет перенаправления в личный кабинет и
   система выдаст информационное сообщение об ошибке логина и пароля, а кнопка "Забыл пароль" перекрасится в оранжевый цвет'''

   page = AuthPage(selenium)
   page.enter_auth_field(data)
   page.driver.implicitly_wait(10)
   page.enter_pass("incorrect password")
   page.driver.implicitly_wait(10)
   page.btn_click()
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль" \
          and page.driver.find_element(By.CLASS_NAME, "login-form__forgot-pwd--animated")


def test_automatic_tab_switching(selenium):
   '''Тест ТС-003. Проверяем, что при введении разного формата данных в поле ввода на странице авторизации,
   таб выбора способа авторизации меняется автоматически'''

   page = AuthPage(selenium)

   page.enter_auth_field(valid_email)
   page.driver.implicitly_wait(10)
   page.enter_pass(" ")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_email.text

   page.enter_auth_field(Keys.CONTROL+'a')
   page.enter_auth_field(Keys.DELETE)

   page.enter_auth_field(valid_phone)
   page.driver.implicitly_wait(10)
   page.enter_pass(" ")

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_phone.text

   page.enter_auth_field(Keys.CONTROL + 'a')
   page.enter_auth_field(Keys.DELETE)

   page.enter_auth_field(valid_login)
   page.driver.implicitly_wait(10)
   page.enter_pass(" ")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_login.text

   page.enter_auth_field(Keys.CONTROL + 'a')
   page.enter_auth_field(Keys.DELETE)

   page.enter_auth_field(valid_ls)
   page.driver.implicitly_wait(10)
   page.enter_pass(" ")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_ls.text


def test_tab_by_default(selenium):
   '''Тест ТС-004. Проверка того, что по умолчанию выбрана форма авторизации  по номеру телефону'''

   page = AuthPage(selenium)

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_phone.text



def generate_string(n): #вспомогательная функция для генерации строки с требуемым количеством символов
   return "x" * n
@pytest.mark.parametrize('input_mail', ["abcdefgh",
                                        "№$#!@*",
                                        "123456789",
                                        "абвгдежсийклмнопрст",
                                        generate_string(255),
                                        generate_string(1001)])
def test_enter_incorrect_data_to_email_field(selenium, input_mail):
   '''Тест ТС-005. Проверка поля "Электронная почта" на ввод некорректных данных и пустой строки'''

   page = AuthPage(selenium)

   page.tab_email_click()

   page.enter_auth_field(input_mail+"\n")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.XPATH, "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]").text == "Неверный формат адреса email"

def test_phone_field_with_shot_number(selenium):
   '''Тест ТС-006. Проверка поля "Мобильный телефон" на ввод слишком короткого номера телефона'''

   page = AuthPage(selenium)

   page.tab_phone_click()
   page.enter_auth_field("12345"+"\n")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-input-container__meta--error").text == "Неверный формат телефона"


def test_ls_field_with_shot_number(selenium):
   '''Тест ТС-007. Проверка поля "Лицевой счет" на ввод слишком короткого лицевого счета'''

   page = AuthPage(selenium)

   page.tab_ls_click()
   page.enter_auth_field("12345"+"\n")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-input-container__meta--error").text ==\
          "Проверьте, пожалуйста, номер лицевого счета"

def test_empty_field_in_login(selenium):
   '''Тест ТС-008. Проверка полей "Мобильный телефон"/"Электронная почта"/"Логин"/"Лицевой счет" на ввод пустой строки'''

   page = AuthPage(selenium)

   page.tab_email_click()
   page.enter_auth_field(""+"\n")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.XPATH,
                                   "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]").text == "Введите адрес, указанный при регистрации"

   page.tab_phone_click()
   page.enter_auth_field(""+"\n")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.XPATH,
                                   "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]").text == "Введите номер телефона"

   page.tab_login_click()
   page.enter_auth_field("" + "\n")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.XPATH,
                                   "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]").text == "Введите логин, указанный при регистрации"

   page.tab_ls_click()
   page.enter_auth_field("" + "\n")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.XPATH,
                                   "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]").text == "Введите номер вашего лицевого счета"

def test_names_of_tabs(selenium):
   '''Тест ТС-009. Проверка соответсвия названий табов заявленным требованиям БАГ-BR-2'''

   page = AuthPage(selenium)

   assert page.tab_email.text == "Почта"
   assert page.tab_phone.text == "Номер"
   assert page.tab_ls.text == "Лицевой счет"
   assert page.tab_ls.text == "Логин"


def test_checkbox(selenium):
   '''Тест ТС-010. Проверка чекбокса "Запомнить пароль" на главной странице авторизации'''

   page = AuthPage(selenium)
   page.driver.find_element(By.CLASS_NAME, "rt-checkbox--checked").click()
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-checkbox")


@pytest.mark.parametrize('login', [valid_phone, valid_email])
def test_temporary_code_authorization_valid_data(selenium, login):
   '''Тест ТС-011. Проверка успешной авторизации зарегистрированного пользователя по временному коду на телефон или почту'''

   page = AuthPageCode(selenium)
   page.driver.implicitly_wait(20)
   page.enter_mail_phone_fild(login)
   page.btn_get_code_click()

   sleep(100) #для ручного ввода корректного полученного кода

   assert page.driver.find_element(By.CLASS_NAME, "lfjrSy").text == "Личный кабинет"


def generate_string(n): #вспомогательная функция для генерации строки с требуемым количеством символов
   return "x" * n
@pytest.mark.parametrize('anvalid_data', ["abcdefgh",
                                        "№$#!@*",
                                        "123456789",
                                        "абвгдежсийклмнопрст",
                                        generate_string(255),
                                        generate_string(1001),
                                        ""])
def test_temporary_code_authorization_unvalid_data(selenium, anvalid_data):
   '''Тест ТС-012. Ввод в поле "E-mail или мобильный телефон" неверных данных'''

   page = AuthPageCode(selenium)
   page.driver.implicitly_wait(30)
   page.enter_mail_phone_fild(anvalid_data)
   page.btn_get_code_click()

   assert page.driver.find_element(By.CLASS_NAME, "rt-input-container__meta--error").text ==\
          "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


def test_btn_auth_with_password(selenium):
   '''Тест ТС-013. Проверка кнопки "Войти с паролем" на странице авторизации по временному коду'''

   page = AuthPageCode(selenium)
   page.driver.implicitly_wait(30)
   page.btn_password_click()

   assert page.driver.find_element(By.CLASS_NAME, "card-container__title").text == "Авторизация"




