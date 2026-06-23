from time import sleep
import pytest
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class TestShoppingCart:

    @pytest.fixture()
    def setup(self):
        #beforeeach
        webdriver = Firefox()

        webdriver.get("https://www.saucedemo.com/")
        webdriver.find_element(By.ID, "user-name").send_keys("standard_user")
        webdriver.find_element(By.ID, "password").send_keys("secret_sauce")
        webdriver.find_element(By.ID, "login-button").click()
        yield webdriver

        #aftereach

        # webdriver.implicitly_wait(10)
        inventory_list = webdriver.find_element(By.CLASS_NAME, "inventory_list")
        assert inventory_list.is_displayed() == True
  

        # sleep(10)
        webdriver.quit()


    
    def test_should_add_item(self,setup:WebDriver):
        webdriver = setup
        buttons_add = webdriver.find_elements(By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
        assert  len(buttons_add) > 0

        first_product = buttons_add[0]
        first_product.click()

        webdriver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        current_url = webdriver.current_url
        assert "cart" in current_url
      
        products_added = webdriver.find_elements(By.CLASS_NAME,"cart_item")
        products_in_cart = len(products_added)
        assert products_in_cart == 1
        
