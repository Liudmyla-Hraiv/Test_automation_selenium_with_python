
import pytest
import selenium.webdriver

@pytest.fixture
def browser():

  # Initialize the WebDriver
  b = selenium.webdriver.Chrome()
  b.implicitly_wait(10)

  yield b
  b.quit()