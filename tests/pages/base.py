from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def load(self):
        self.browser.get(self.URL)

    def wait(self, *element):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(element)
            )
        except:
            self.browser.quit()