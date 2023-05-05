from .base_page import BasePage
from .locators import Registration



class Registr(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = "https://b2c.passport.rt.ru"
       driver.get(url)

       #self.find_name = driver.find_element(*Registration.NAME)
       #self.find_surname = driver.find_element(*Registration.SURNAME)

       #self.find_region = driver.find_element(*Registration.REGION)

       #self.find_phone_or_mail = driver.find_element(*Registration.MAIL_OR_PHONE)

       #self.find_password = driver.find_element(*Registration.PASSWORD)
       #self.find_confirm = driver.find_element(*Registration.PASSWORD_CONFIRM)

       #self.find_btn_registr = driver.find_element(*Registration.BTN_REGISTR)


  # def enter_name(self, value):
      # self.find_name.send_keys(value)

   #def enter_surname(self, value):
    #   self.find_surnamename.send_keys(value)

   #def enter_region(self, value):
   #    self.find_region.send_keys(value)

  # def enter_mail_or_phone(self, value):
       #self.find_phone_or_mail.send_keys(value)

   #def enter_password(self, value):
       #self.find_password.send_keys(value)

   #def enter_password_confirm(self, value):
       #self.find_confirm.send_keys(value)

  # def click_btn_registr(self, value):
       #self.find_btn_registr.click()

