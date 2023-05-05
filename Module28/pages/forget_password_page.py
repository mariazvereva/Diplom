from .base_page import BasePage
from .locators import PasswordRecoveryLocators



class ForgetPasswordPage(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"
       driver.get(url)

       self.find_field = driver.find_element(*PasswordRecoveryLocators.FIELD)

       self.tab_email = driver.find_element(*PasswordRecoveryLocators.TAB_MAIL_RE)
       self.tab_phone = driver.find_element(*PasswordRecoveryLocators.TAB_PHONE_RE)
       self.tab_login = driver.find_element(*PasswordRecoveryLocators.TAB_LOGIN_RE)
       self.tab_ls = driver.find_element(*PasswordRecoveryLocators.TAB_LS_RE)


       self.find_field_captcha = driver.find_element(*PasswordRecoveryLocators.FIELD_CAPTCHA)
       self.btn_continue = driver.find_element(*PasswordRecoveryLocators.BTN_CONTINUE)
       self.btn_come_back = driver.find_element(*PasswordRecoveryLocators.BTN_COME_BACK)

       # self.btn_radiobtn_phone = driver.find_element(*PasswordRecoveryLocators.RADIOBTN_PHONE)
       #self.btn_radiobtn_email = driver.find_element(*PasswordRecoveryLocators.RADIOBTN_EMAIL)
       #self.btn_continue_2page = driver.find_element(*PasswordRecoveryLocators.BTN_CONTINUE_2PAGE)
       #self.btn_come_back_2page = driver.find_element(*PasswordRecoveryLocators.BTN_COME_BACK_2PAGE)

       #self.btn_come_back_3page = driver.find_element(*PasswordRecoveryLocators.BTN_COME_BACK_3PAGE)

       #self.field_new_password = driver.find_element(*PasswordRecoveryLocators.FIELD_NEW_PASSWORD)
       #self.field_new_password_confirm = driver.find_element(*PasswordRecoveryLocators.FIELD_NEW_PASSWORD_CONFIRM)
       #self.btn_save_new_password = driver.find_element(*PasswordRecoveryLocators.BTN_SAVE_NEW_PASSWORD)


   def enter_field(self, value):
       self.find_field.send_keys(value)

   def enter_captcha(self, value):
       self.find_field_captcha.send_keys(value)

   def btn_continue_click(self):
       self.btn_continue.click()

   #def btn_continue_2page_click(self):
       #self.btn_continue_2page.click()

   def btn_come_back_click(self):
       self.btn_come_back.click()

   #def btn_come_back_2page_click(self):
       #self.btn_come_back_2page.click()

   #def btn_come_back_3page_click(self):
       #self.btn_come_back_3page.click()

   #def btn_radiobtn_phone_click(self):
       #self.btn_radiobtn_phone.click()

   #def btn_radiobtn_email_click(self):
       #self.btn_radiobtn_email.click()

   #def enter_field_new_password(self, value):
       #self.field_new_password.send_keys(value)

   #def enter_field_new_password_confirm(self, value):
       #self.field_new_password_confirm.send_keys(value)

   #def btn_save_new_password_click(self):
       #self.btn_save_new_password.click()

