import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from ConfigReader import ConfigReader
from browser import Browser

config = ConfigReader()


@pytest.mark.parametrize("language", ["ru", "en"])
@pytest.mark.parametrize("game_name, n", [("The Witcher", 10), ("Fallout", 20)])
def test_steam_search(language, game_name, n):
    driver = Browser.get_driver(language)

    driver.get(config.get('BASE_URL'))

    home_page = HomePage()
    home_page.wait_for_page_to_load()
    home_page.search(game_name)

    search_page = SearchResultsPage()
    search_page.wait_for_page_to_load()
    search_page.set_sort_by_price_desc()

    top_n_games = search_page.get_first_n_games(n)
    prices = search_page.get_game_prices(top_n_games)

    for i in range(len(prices) - 1):
        assert prices[i] >= prices[i + 1], \
            f"Ошибка сортировки на позициях {i} и {i + 1}!\n" \
            f"{prices[i]} < {prices[i + 1]}\n" \
            f"Все первые {n} цен: {prices}"

    print(f"  ✓ СОРТИРОВКА КОРРЕКТНА: первые {n} цен: {prices}")
