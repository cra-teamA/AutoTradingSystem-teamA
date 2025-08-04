import pytest
from auto_trading_system import AutoTradingSystem
from driver_kiwer import KiwerDriver
from nemo_driver import NemoDriver
from stocker_brocker_driver_interface import StockBrockerDriverInterface

ID = "id"
PW = "pw"
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000


@pytest.fixture
def nemo_interface(mocker):
    driver = NemoDriver()
    driverif = StockBrockerDriverInterface(driver)
    driverif.login(ID, PW)
    ats = AutoTradingSystem()
    ats.selectStockBrocker(driverif)
    return ats, driverif

@pytest.fixture
def kiwer_interface(mocker):
    driver = NemoDriver()
    driverif = StockBrockerDriverInterface(driver)
    driverif.login(ID, PW)
    ats = AutoTradingSystem()
    ats.selectStockBrocker(driverif)
    return ats, driverif

def test_ats_login_with_nemo():
    driver = KiwerDriver()
    driverif = StockBrockerDriverInterface(driver)
    ats = AutoTradingSystem()
    ats.selectStockBrocker(driverif)
    try:
        ats.login(ID, PW)
    except:
        pytest.fail()


def test_ats_buy_with_nemo(nemo_interface):
    ats, interface = nemo_interface

    try:
        ats.buy(STOCK, PRICE, COUNT)
    except:
        pytest.fail()

def test_ats_sell_with_nemo(nemo_interface):
    ats, interface = nemo_interface

    try:
        ats.sell(STOCK, PRICE, COUNT)
    except:
        pytest.fail()

def test_ats_get_price_with_nemo(nemo_interface):
    ats, interface = nemo_interface

    try:
        ats.getPrice(STOCK)
    except:
        pytest.fail()

def test_ats_login_with_kiwer():
    driver = KiwerDriver()
    driverif = StockBrockerDriverInterface(driver)
    ats = AutoTradingSystem()
    ats.selectStockBrocker(driverif)
    try:
        ats.login(ID, PW)
    except:
        pytest.fail()


def test_ats_buy_with_kiwer(kiwer_interface):
    ats, interface = kiwer_interface

    try:
        ats.buy(STOCK, PRICE, COUNT)
    except:
        pytest.fail()

def test_ats_sell_with_kiwer(kiwer_interface):
    ats, interface = kiwer_interface

    try:
        ats.sell(STOCK, PRICE, COUNT)
    except:
        pytest.fail()

def test_ats_get_price_with_kiwer(kiwer_interface):
    ats, interface = kiwer_interface

    try:
        ats.getPrice(STOCK)
    except:
        pytest.fail()
