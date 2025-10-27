from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verificar_productos(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        nombres = [item.text for item in items]
        return nombres
