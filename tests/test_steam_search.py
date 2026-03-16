import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from ConfigReader import ConfigReader

config = ConfigReader()



@pytest.mark.parametrize("language, game_name, n", [
    ("ru", "The Witcher", 10),
    ("ru", "Fallout", 20),
    ("en", "The Witcher", 10),
    ("en", "Fallout", 20),
])
def test_steam_search(language, game_name, n, driver):
    driver.get(config.get('BASE_URL'))

    home_page = HomePage(driver)
    home_page.wait_for_page_to_load()

    home_page.search(game_name)

    search_page = SearchResultsPage(driver)
    search_page.wait_for_page_to_load()
    search_page.set_sort_by_price_desc()

    top_n_games = search_page.get_first_n_games(n)
    prices = search_page.get_game_prices(top_n_games)

    sorted_prices = sorted(prices, reverse=True)
    assert prices == sorted_prices, \
        f"ОШИБКА СОРТИРОВКИ!\n" \
        f"Первые {n} цен: {prices}\n" \
        f"Ожидалось: {sorted_prices}"

    print(f"  ✓ СОРТИРОВКА КОРРЕКТНА: первые {n} цен: {prices}")
