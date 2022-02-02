import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./browser-drivers/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(By.CLASS_NAME, 'added-manually')
                delete_button.click()
            except:
                print('You are trying to delete more elements that the existent')
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen ")
        if total_elements < 1:
            print("There are 0 elements on screen")

        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
