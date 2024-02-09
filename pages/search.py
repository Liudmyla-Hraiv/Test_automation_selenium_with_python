
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchPage:

  URL = 'https://www.youtube.com/'
  COOKIES = (By.XPATH, '(//button[@class=\'yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m\'])[2]' )
  SEARCH_INPUT = (By.XPATH, '//input[@id=\'search\']')
  
  # Initializer
  def __init__(self, browser):
    self.browser = browser

  # Methods
  def load(self):
    self.browser.get(self.URL)
    self.browser.find_element(*self.COOKIES).click()
    self.browser.implicitly_wait(1)

  def search(self, phrase):
    self.browser.implicitly_wait(1)
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase)
    search_input.send_keys(Keys.RETURN)
    self.browser.implicitly_wait(1)

    