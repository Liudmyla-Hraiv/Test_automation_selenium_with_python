
import pytest

from pages.result import ResultPage
from pages.search import SearchPage


@pytest.mark.parametrize('phrase', ['duck', 'goose', 'panda'])
def test_basic_search(browser, phrase):
  search_page = SearchPage(browser)
  result_page = ResultPage(browser)
  
  search_page.load()

  search_page.search(phrase)

  assert phrase == result_page.search_input_value()
  
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0

  assert phrase in result_page.title()


