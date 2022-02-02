import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./browser-drivers/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()

    def test_add_remove(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i + 1} is NOT FOUND")
                    tries = tries + 1
                    driver.refresh()

            print(f"Finished in {tries} tries")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
