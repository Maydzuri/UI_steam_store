import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config import BASE_URL


test_data = [
    ("ru", "The Witcher", 10),
    ("ru", "Fallout", 20),
    ("en", "The Witcher", 10),
    ("en", "Fallout", 20),
]


@pytest.mark.parametrize("language, game_name, n", test_data)
def test_steam_search(language, game_name, n, driver):
    home_page = HomePage(driver)
    home_page.open(BASE_URL)

    home_page.search(game_name)

    search_page = SearchResultsPage(driver)
    search_page.set_sort_by_price_desc()

    games = search_page.get_first_n_games(n)

    assert len(games) == n, f"Ожидалось {n} игр, получено {len(games)}"

    prices = search_page.get_game_prices(games)
    if prices and any(p > 0 for p in prices):
        assert prices == sorted(prices, reverse=True), "Ошибка сортировки по цене"
