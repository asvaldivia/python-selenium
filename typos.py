import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./browser-drivers/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Typos').click()

    def test_typos(self):
        # Cuantos intentos nos toma encontrar el typo?
        driver = self.driver

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while not found or tries > 100:
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            if correct_text == text_to_check:
                tries += 1
                driver.refresh()
            if correct_text != text_to_check:
                found = True
        self.assertEqual(found, True)
        print(f"It took {tries} tries to find the typo")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
