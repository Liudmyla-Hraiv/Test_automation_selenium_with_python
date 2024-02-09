
from selenium.webdriver.common.by import By


class ResultPage:
  
  # Locators

  RESULT_LINKS = (By.XPATH, '//ytd-video-renderer[@class = \'style-scope ytd-item-section-renderer\']')
  SEARCH_INPUT = (By.XPATH, '//input[@id=\'search\']')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def result_link_titles(self):
    links = self.browser.find_elements(*self.RESULT_LINKS)
    titles = [link.text for link in links]
    return titles
  
  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    value = search_input.get_attribute('value')
    return value

  def title(self):
    return self.browser.title