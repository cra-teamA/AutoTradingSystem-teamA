import pytest
from pytest_mock import MockFixture

from stocker_brocker_driver_interface import StockBrockerDriverInterface

ID = 'id'
PW = 'pw'
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000


@pytest.fixture
def driver_interface_data_with_login(mocker):
    driver = mocker.Mock()
    driver_interface = StockBrockerDriverInterface(driver)
    driver_interface.login(ID, PW)
    return driver_interface, driver


@pytest.fixture
def driver_interface_data_without_login(mocker):
    driver = mocker.Mock()
    driver_interface = StockBrockerDriverInterface(driver)
    return driver_interface, driver


def test_interface_creation(driver_interface_data_with_login):
    driver_interface, driver = driver_interface_data_with_login
    assert driver_interface is not None


def test_login(capsys, driver_interface_data_without_login):
    driver_interface, driver = driver_interface_data_without_login
    try:
        driver_interface.login(ID, PW)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'login' in catured.out
    assert driver.login.called == 1


def test_login_fail(capsys, driver_interface_data_with_login):
    driver_interface, driver = driver_interface_data_with_login
    with pytest.raises(Exception):
        driver_interface.login(ID, PW)

    catured = capsys.readouterr()
    assert 'already logined' in catured.out
    assert driver.login.called == 1


def test_get(driver_interface_data_with_login):
    driver_interface, driver = driver_interface_data_with_login
    driver.get_price.return_value = 1
    ret = driver_interface.get(STOCK)
    assert isinstance(ret, int)
    assert driver.get_price.called == 1

def test_get_fail(driver_interface_data_without_login):
    driver_interface, driver = driver_interface_data_without_login
    driver.get_price.return_value = 1
    with pytest.raises(Exception, match="Please login"):
        ret = driver_interface.get(STOCK)


def test_buy(capsys, driver_interface_data_with_login):
    driver_interface, driver = driver_interface_data_with_login
    driver.buy.return_value = print('Buy stock')
    try:
        driver_interface.buy(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'stock' in catured.out
    assert driver.buy.called == 1

def test_buy_fail(capsys, driver_interface_data_without_login):
    driver_interface, driver = driver_interface_data_without_login
    with pytest.raises(Exception, match="Please login"):
        driver_interface.buy(STOCK, COUNT, PRICE)


def test_sell(capsys, driver_interface_data_with_login):
    driver_interface, driver = driver_interface_data_with_login
    driver.sell.return_value = print('Sell stock')

    try:
        driver_interface.sell(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'stock' in catured.out
    assert driver.sell.called == 1

def test_sell_fail(capsys, driver_interface_data_without_login):
    driver_interface, driver = driver_interface_data_without_login

    with pytest.raises(Exception, match="Please login"):
        driver_interface.sell(STOCK, COUNT, PRICE)
