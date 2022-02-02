import unittest
from selenium import webdriver
from mercado_libre_page import MercadoLibrePage


class CompareProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'../../browser-drivers/chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        mcl = MercadoLibrePage(self.driver)
        mcl.open()
        self.assertTrue(mcl.is_loaded)
        mcl.choise_contry('colombia')
        mcl.search('playstation 4')
        mcl.choise_filter('nuevo')
        mcl.choise_filter('Bogotá D.C.')
        mcl.choise_order_by('Mayor precio')
        print(mcl.get_top_5_elements_result())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
