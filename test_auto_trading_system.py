import pytest
from auto_trading_system import AutoTradingSystem

ID = "id"
PW = "pw"
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000


@pytest.fixture
def ats_with_mock_interface(mocker):
    mock_interface = mocker.Mock()
    ats = AutoTradingSystem()
    ats.selectStockBrocker(mock_interface)
    return ats, mock_interface


def test_ats_login(ats_with_mock_interface):
    ats, inteface = ats_with_mock_interface

    ats.login(ID, PW)

    inteface.login.assert_called_once_with(ID, PW)


def test_ats_buy(ats_with_mock_interface):
    ats, interface = ats_with_mock_interface

    ats.buy(STOCK, PRICE, COUNT)

    interface.buy.assert_called_once_with(STOCK, PRICE, COUNT)


def test_ats_sell(ats_with_mock_interface):
    ats, interface = ats_with_mock_interface

    ats.sell(STOCK, PRICE, COUNT)

    interface.sell.assert_called_once_with(STOCK, PRICE, COUNT)

def test_get_Price(ats_with_mock_interface):
    ats, interface = ats_with_mock_interface
    interface.get.return_value = 1000
    assert ats.getPrice(STOCK) == 1000

@pytest.mark.parametrize("lst",
[(10,12,14)]
 )
def test_getbuyNiceTiming(ats_with_mock_interface, lst):
    ats, interface = ats_with_mock_interface
    interface.get.side_effect = lst
    ats.getbuyNiceTiming(STOCK, PRICE)
    assert interface.get.call_count == 3
    interface.buy.assert_called_once_with(STOCK,PRICE//14,14)

@pytest.mark.parametrize("lst",
[(10,8,6)]
 )
def test_sellNiceTiming(ats_with_mock_interface, lst):
    ats, interface = ats_with_mock_interface
    interface.get.side_effect = lst
    ats.sellNiceTiming(STOCK, COUNT)
    assert interface.get.call_count == 3
    interface.sell.assert_called_once_with(STOCK,COUNT,6)
