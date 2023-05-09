from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


class TestCEO:
    def setup_method(self):
        options = Options()
        options.add_argument("headless")
        self.driver = webdriver.Edge(options=options)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_ceo(self):
        # Test name: test_ceo
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1000, 600)
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("JD")
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("CEO")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".display-6").text
            == "Hello Chief Happiness Officer"
        )
