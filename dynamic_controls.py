import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep


class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./browser-drivers/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
        checkbox.click()

        remove_add_button = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add_button.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, '#input-example > button')
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.send_keys('Hola, esa no es mi paloma es mi pistola')
        sleep(3)
        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
