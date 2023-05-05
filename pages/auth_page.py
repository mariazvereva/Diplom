from .base_page import BasePage
from .locators import AuthLocators, AuthLocatorsCode,PasswordRecoveryLocators



class AuthPage(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = "https://b2c.passport.rt.ru"
       driver.get(url)

       self.find_field = driver.find_element(*AuthLocators.AUTH_FIELD)

       self.tab_email = driver.find_element(*AuthLocators.TAB_MAIL)
       self.tab_phone = driver.find_element(*AuthLocators.TAB_PHONE)
       self.tab_login = driver.find_element(*AuthLocators.TAB_LOGIN)
       self.tab_ls = driver.find_element(*AuthLocators.TAB_LS)


       self.password = driver.find_element(*AuthLocators.AUTH_PASS)
       self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
       self.btn_forget_password = driver.find_element(*AuthLocators.BTN_FORGET_PASSWORD)


   def enter_auth_field(self, value):
       self.find_field.send_keys(value)

   def enter_pass(self, value):
       self.password.send_keys(value)

   def btn_click(self):
       self.btn.click()

   def tab_email_click(self):
       self.tab_email.click()

   def tab_phone_click(self):
       self.tab_phone.click()

   def tab_ls_click(self):
       self.tab_ls.click()

   def tab_login_click(self):
       self.tab_login.click()

   def dtn_forget_password_click(self):
       self.btn_forget_password.click()

class AuthPageCode(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light"
       driver.get(url)

       self.mail_phone_fild = driver.find_element(*AuthLocatorsCode.EMAIL_PHONE_FIELD)
       self.btn_get_code = driver.find_element(*AuthLocatorsCode.BTN_GET_CODE)
       self.btn_password = driver.find_element(*AuthLocatorsCode.BTN_AUTH_PASS)

   def enter_mail_phone_fild(self, value):
       self.mail_phone_fild.send_keys(value)

   def btn_get_code_click(self):
       self.btn_get_code.click()

   def btn_password_click(self):
       self.btn_password.click()