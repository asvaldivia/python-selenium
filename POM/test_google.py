import unittest
from selenium import webdriver
from google_page import GooglePage


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'../browser-drivers/chromedriver.exe')
        driver = cls.driver
        driver.maximize_window()

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.is_loaded
        google.search('platzi')

        self.assertEqual('platzi', google.keyword)

    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
