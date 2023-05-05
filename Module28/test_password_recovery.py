import pytest
from pages.forget_password_page import ForgetPasswordPage
from settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.parametrize('data', [valid_phone, valid_email])
def test_recovery_password_with_valid_data(selenium, data):
   '''Тест ТС-014. Проверяем, что зарегистрированный в системе пользователь может успешно
   поменять пароль через форму восстановления пароля'''

   page = ForgetPasswordPage(selenium)

   page.enter_field(data)
   page.driver.implicitly_wait(10)

   sleep(30) #для ввода капчи

   page.btn_continue_click()

   if data == valid_phone:
      page.driver.find_element(By.XPATH,
                               "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/label[1]/span[1]/span[1]").click()
   else:
      page.driver.find_element(By.XPATH,
                               "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/label[2]/span[1]/span[3]/span[1]").click()


   page.driver.find_element(By.CLASS_NAME, "reset-choice-form__reset-btn").click()

   sleep(100)  # для ввода кода
   wait = WebDriverWait(page.driver, 100).until(EC.visibility_of_element_located((By.ID, "password-new")))
   page.driver.find_element(By.ID, "password-new").send_keys("987654Ma")
   page.driver.implicitly_wait(10)
   page.driver.find_element(By.ID, "password-confirm").send_keys("987654Ma")
   page.driver.implicitly_wait(10)
   page.driver.find_element(By.ID, "t-btn-reset-pass").click()
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "card-container__title") == "Авторизация"




def test_recovery_password_with_email_only(selenium):
   '''Тест ТС-015. Проверяем, что, если  в учетной записи прикреплена только электронная почта (без телефона)
   ,то система сразу переходит к сценарию восстановления пароля по номеру телефона
   (не переходя к окну выбора варинта воостановления пароля)'''

   page = ForgetPasswordPage(selenium)

   page.enter_field(valid_email_2)
   page.driver.implicitly_wait(10)

   sleep(30) #для ввода капчи

   page.btn_continue_click()


   assert page.driver.find_element(By.CLASS_NAME, "reset-confirm-form")


def test_automatic_tab_switch_reset_password_page(selenium):
   '''Тест ТС-016. Проверяем, что при введении разного формата данных на странице восстановления пароля,
   таб выбора способа авторизации меняется автоматически'''

   page = ForgetPasswordPage(selenium)

   page.enter_field(valid_email)
   page.driver.implicitly_wait(10)
   page.enter_captcha(" ")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_email.text

   page.enter_field(Keys.CONTROL+'a')
   page.enter_field(Keys.DELETE)

   page.enter_field(valid_phone)
   page.driver.implicitly_wait(10)
   page.enter_captcha(" ")

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_phone.text

   page.enter_field(Keys.CONTROL + 'a')
   page.enter_field(Keys.DELETE)

   page.enter_field(valid_login)
   page.driver.implicitly_wait(10)
   page.enter_captcha(" ")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_login.text

   page.enter_field(Keys.CONTROL + 'a')
   page.enter_field(Keys.DELETE)

   page.enter_field(valid_ls)
   page.driver.implicitly_wait(10)
   page.enter_captcha(" ")
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_ls.text


def test_tab_by_default_reset_password_page(selenium):
   '''Тест ТС-017. Проверка того, что по умолчанию выбран таб по номеру телефону'''

   page = ForgetPasswordPage(selenium)

   assert page.driver.find_element(By.CLASS_NAME, "rt-tab.rt-tab--small.rt-tab--active").text == page.tab_phone.text


def test_recovery_password_with_unvalid_data(selenium):
   '''Тест ТС-018. Проверяем, что при попытке восстановления пароля
   незарегистрированным в системе пользователем и вводе не совпадающей с картинкой капчи
   системой выводится информационное сообщение с ошибкой'''

   page = ForgetPasswordPage(selenium)

   page.enter_field("абвг@mail.ru")
   page.driver.implicitly_wait(10)
   page.enter_captcha("12345")
   page.driver.implicitly_wait(10)
   page.btn_continue_click()
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.ID, "form-error-message").text == "Неверный логин или текст с картинки"


def test_back_button(selenium):
   '''Тест ТС-019. Проверяем, что нопка "Вернуться назад" ведет на страницу авторизации'''

   page = ForgetPasswordPage(selenium)


   page.btn_come_back_click()
   page.driver.implicitly_wait(10)

   assert page.driver.find_element(By.CLASS_NAME, "card-container__title").text == "Авторизация"