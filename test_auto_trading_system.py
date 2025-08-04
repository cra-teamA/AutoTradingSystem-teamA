import pytest
from auto_trading_system import AutoTradingSystem

ID = "id"
PW = "pw"
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000


@pytest.fixture
def ats_with_mock_driver(mocker):
    mock_driver = mocker.Mock()
    ats = AutoTradingSystem()
    ats.selectStockBrocker(mock_driver)
    return ats, mock_driver


def test_ats_login(ats_with_mock_driver):
    ats, driver = ats_with_mock_driver

    ats.login(ID, PW)

    driver.login.assert_called_once_with(ID, PW)


def test_ats_buy(ats_with_mock_driver):
    ats, driver = ats_with_mock_driver

    ats.buy(STOCK, PRICE, COUNT)

    driver.buy.assert_called_once_with(STOCK, PRICE, COUNT)


def test_ats_sell(ats_with_mock_driver):
    ats, driver = ats_with_mock_driver

    ats.sell(STOCK, PRICE, COUNT)

    driver.sell.assert_called_once_with(STOCK, PRICE, COUNT)