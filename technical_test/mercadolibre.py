import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestingMercadoLibre(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'../browser-drivers/chromedriver.exe')
        driver = cls.driver
        driver.maximize_window()
        driver.get('https://mercadolibre.com/')

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element(By.ID, 'CO')
        country.click()

        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playsation 4')
        search_field.submit()

        location = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div/aside/section/div[10]/ul/li[1]/a/span[1]')
        driver.execute_script("arguments[0].click();", location)

        condition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        driver.execute_script("arguments[0].click();", condition)

        order_menu = driver.find_element(By.CLASS_NAME, 'andes-dropdown__trigger')
        order_menu.get_property()
        order_menu.click()
        higher_price = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/div/ul/a[2]')
        higher_price.click()

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        print(articles, prices)

    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
