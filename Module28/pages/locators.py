from selenium.webdriver.common.by import By

class AuthLocators:

   TAB_PHONE = (By.ID, "t-btn-tab-phone")
   TAB_MAIL = (By.ID, "t-btn-tab-mail")
   TAB_LOGIN = (By.ID, "t-btn-tab-login")
   TAB_LS = (By.ID, "t-btn-tab-ls")

   AUTH_FIELD = (By.ID, "username")
   AUTH_PASS = (By.ID, "password")

   AUTH_BTN = (By.ID, "kc-login")

   BTN_FORGET_PASSWORD = (By.ID, "forgot_password")


class AuthLocatorsCode:

   EMAIL_PHONE_FIELD = (By.ID, "address")
   BTN_GET_CODE = (By.ID, "otp_get_code")
   BTN_AUTH_PASS = (By.ID, "standard_auth_btn")

class PasswordRecoveryLocators:

   TAB_PHONE_RE = (By.ID, "t-btn-tab-phone")
   TAB_MAIL_RE = (By.ID, "t-btn-tab-mail")
   TAB_LOGIN_RE = (By.ID, "t-btn-tab-login")
   TAB_LS_RE = (By.ID, "t-btn-tab-ls")

   FIELD = (By.ID, "username")
   FIELD_CAPTCHA = (By.ID, "captcha")
   BTN_CONTINUE = (By.ID, "reset")
   BTN_COME_BACK = (By.ID, "reset-back")

   #RADIOBTN_PHONE = (By.LINK_TEXT, "По номеру телефона")
   #RADIOBTN_EMAIL = (By.XPATH, "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/label[2]/span[1]/span[3]/span[1]")
   #BTN_CONTINUE_2PAGE = (By.CLASS_NAME, "reset-choice-form__reset-btn")
   #BTN_COME_BACK_2PAGE = (By.CLASS_NAME, 'reset-choice-form__back-btn')

   #BTN_COME_BACK_3PAGE = (By.CLASS_NAME, 'reset-confirm-form__back-btn')

   #FIELD_NEW_PASSWORD = (By.ID, "password-new")
   #FIELD_NEW_PASSWORD_CONFIRM = (By.ID, "password-confirm")
   #BTN_SAVE_NEW_PASSWORD = (By.ID, "t-btn-reset-pass")


class Registration:

   NAME = (By.XPATH, '//input[@name="firstName"]')
   SURNAME = (By.XPATH, '//input[@name="lastName"]')
   REGION = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]')
   MAIL_OR_PHONE = (By.ID, 'address')
   PASSWORD = (By.ID, 'password')
   PASSWORD_CONFIRM = (By.ID, 'password-confirm')
   BTN_REGISTR = (By.CLASS_NAME, 'register-form__reg-btn')
