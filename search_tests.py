import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./browser-drivers/chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        # limpia el campo de búsqueda en caso de que haya algún texto.
        search_field.clear()
        # simulamos la escritura del teclado para poner "tee"
        search_field.send_keys('tee')
        #envía los datos ('tee') para que la página muestre los resultados de "tee"
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()
        # hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
        products = driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div['
                                                  '3]/ul/li/div/h2/a')
        # vamos a preguntar si la cantidad de resultados es igual a 1
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
