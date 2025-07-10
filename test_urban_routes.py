from data import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp
from utils import retrieve_code as rc

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import ChromeOptions

        options = ChromeOptions()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_pages = urp.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_pages.set_route(address_from, address_to)
        assert self.routes_pages.get_from() == address_from
        assert self.routes_pages.get_to() == address_to

    def test_select_comfort_tariff(self):
        self.routes_pages.click_order_a_cab()
        self.routes_pages.click_Comfort_card()
        selected_card = self.driver.find_element(By.XPATH, "//div[@class='tcard active']//div[text()='Comfort']")
        assert selected_card is not None

    def test_add_phone_number(self):
        self.routes_pages.click_select_phone_number()
        self.routes_pages.input_phone_number()
        self.routes_pages.confirm_phone()
        code = rc.retrieve_phone_code(self.driver)
        self.routes_pages.input_sms_code(code)
        self.routes_pages.click_confirm_sms_code()
        assert "Método de pago" in self.driver.page_source

    def test_add_card_number(self):
        self.routes_pages.click_payment_method()
        self.routes_pages.select_add_card()
        self.routes_pages.add_card_number()
        self.routes_pages.add_card_code()
        self.routes_pages.click_confirm_add_card()
        self.routes_pages.click_close_payment_method()
        assert "Método de pago" in self.driver.page_source

    def test_write_message_to_driver(self):
        self.routes_pages.send_comment_to_driver()
        comment_value = self.driver.find_element(By.ID, "comment").get_attribute("value")
        assert comment_value == "I wear black"

    def test_order_a_blanket_and_tissues(self):
        self.routes_pages.click_manta_y_panuelos()
        checkbox = self.driver.find_element(By.XPATH,"//div[.//div[text()='Manta y pañuelos']]//input[@type='checkbox']")
        assert checkbox.get_attribute("value") == "on"

    def test_order_2_ice_creams(self):
        self.routes_pages.add_2_helados(2)
        counter_value = self.driver.find_element(By.XPATH, "//div[.//div[text()='Helado']]//div[@class='counter-value']").text
        assert counter_value == "2"

    def test_the_cab_search_mode_appears(self):
        self.routes_pages.click_search_driver()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
