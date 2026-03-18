import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from ConfigReader import ConfigReader
from browser import Language

config = ConfigReader()


@pytest.mark.parametrize("language", [Language.RUSSIAN, Language.ENGLISH])
@pytest.mark.parametrize("game_name, n", [("The Witcher", 10), ("Fallout", 20)])
def test_steam_search(language, game_name, n, browser):
    browser.get(config.get('BASE_URL'))

    home_page = HomePage()
    home_page.wait_for_page_to_load()
    home_page.search(game_name)

    search_page = SearchResultsPage()
    search_page.wait_for_page_to_load()
    search_page.set_sort_by_price_desc()

    top_n_games = search_page.get_first_n_games(n)
    prices = search_page.get_game_prices(top_n_games)

    sorted_prices = sorted(prices, reverse=True)
    assert prices == sorted_prices, \
        f"Ошибка сортировки! Первые {n} цен должны идти по убыванию.\n" \
        f"Получено:  {prices}\n" \
        f"Ожидалось: {sorted_prices}"
