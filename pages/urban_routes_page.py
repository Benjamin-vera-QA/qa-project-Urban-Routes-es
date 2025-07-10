import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_a_cab_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    select_comfort_card = (By.XPATH, "//div[@class='tcard'][.//div[text()='Comfort']]")
    select_phone_number = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, "phone")
    confirm_phone_number = (By.XPATH, "//button[@type='submit' and contains(@class, 'button') and contains(@class, 'full')]")
    sms_code_input = (By.ID, "code")
    confirm_sms_button = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card_button = (By.CLASS_NAME, "pp-plus-container")
    number_card_input = (By.ID, "number")
    code_card_input = (By.NAME, "code")
    add_card_confirm_button = (By.XPATH, "//button[text()='Agregar']")
    close_button_payment_method = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    comment_input = (By.ID, "comment")
    manta_y_panuelos_switch = (By.XPATH, "//*[@class='slider round']")
    helado_counter = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    search_driver = (By.CLASS_NAME, "smart-button-wrapper")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        self.wait.until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.visibility_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def get_order_a_cab(self):
        return self.wait.until(EC.presence_of_element_located(self.order_a_cab_button))

    def click_order_a_cab(self):
        self.get_order_a_cab().click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_comfort_card(self):
        return self.wait.until(EC.presence_of_element_located(self.select_comfort_card))

    def click_Comfort_card(self):
        self.get_comfort_card().click()

    def get_select_phone_number(self):
        return self.wait.until(EC.presence_of_element_located(self.select_phone_number))

    def click_select_phone_number(self):
        self.get_select_phone_number().click()

    def get_phone_input(self):
        return self.wait.until(EC.presence_of_element_located(self.phone_input))

    def input_phone_number(self):
        self.get_phone_input().send_keys("+1 123 123 12 12")

    def get_confirm_phone_number(self):
        return self.wait.until(EC.presence_of_element_located(self.confirm_phone_number))

    def confirm_phone(self):
        self.get_confirm_phone_number().click()

    def get_sms_code(self):
        return self.wait.until(EC.presence_of_element_located(self.sms_code_input))

    def input_sms_code(self, code):
        self.get_sms_code().send_keys(code)

    def get_confirm_sms_code(self):
        return self.wait.until(EC.presence_of_element_located(self.confirm_sms_button))

    def click_confirm_sms_code(self):
        self.get_confirm_sms_code().click()

    def get_payment_method(self):
        return self.wait.until(EC.presence_of_element_located(self.payment_method_button))

    def click_payment_method(self):
        self.get_payment_method().click()

    def get_add_card_button(self):
        return self.wait.until(EC.presence_of_element_located(self.add_card_button))

    def select_add_card(self):
        self.get_add_card_button().click()

    def get_card_number(self):
        return self.wait.until(EC.presence_of_element_located(self.number_card_input))

    def add_card_number(self):
        self.get_card_number().send_keys("1234 5678 9100")

    def get_add_card_code(self):
        return self.wait.until(EC.presence_of_element_located(self.code_card_input))

    def add_card_code(self):
        code_field = self.wait.until(EC.element_to_be_clickable(self.code_card_input))
        code_field.clear()
        code_field.send_keys("111" + Keys.TAB)

    def get_confirm_add_card(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_confirm_button))

    def click_confirm_add_card(self):
        self.get_confirm_add_card().click()

    def get_close_button(self):
        return self.wait.until(EC.presence_of_element_located(self.close_button_payment_method))

    def click_close_payment_method(self):
        self.get_close_button().click()

    def get_send_comment_button(self):
        return self.wait.until(EC.presence_of_element_located(self.comment_input))

    def send_comment_to_driver(self):
        self.get_send_comment_button().send_keys("I wear black")

    def get_manta_y_panuelos(self):
        return self.wait.until(EC.presence_of_element_located(self.manta_y_panuelos_switch))

    def click_manta_y_panuelos(self):
        self.get_manta_y_panuelos().click()

    def get_2_helados(self):
        return self.wait.until(EC.presence_of_element_located(self.helado_counter))

    def add_2_helados(self, count=2):
        self.get_2_helados().click()
        self.get_2_helados().click()

    def get_search_driver(self):
        return self.wait.until(EC.presence_of_element_located(self.search_driver))

    def click_search_driver(self):
        self.get_search_driver().click()

