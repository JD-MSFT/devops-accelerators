from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


class TestNamejd:
    def setup_method(self):
        options = Options()
        options.add_argument("headless")
        self.driver = webdriver.Edge(options=options)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_namejd(self):
        # Test name: name-jd
        # Step # | name | target | value | comment
        # 1 | open | https://workshopappjd.azurewebsites.net/ |  |
        self.driver.get("http://127.0.0.1:5005/")
        # 2 | setWindowSize | 966x527 |  |
        self.driver.set_window_size(1000, 600)
        # 3 | click | id=name |  |
        self.driver.find_element(By.ID, "name").click()
        # 4 | type | id=name | JD |
        self.driver.find_element(By.ID, "name").send_keys("JD")
        # 5 | click | css=.btn |  |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
