import pytest
from pytest_mock import MockFixture
from driver_mock import MockDriver


from stocker_brocker_driver_interface import StockBrockerDriverInterface


ID = 'id'
PW = 'pw'
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000

@pytest.fixture
def driver_interface_data(mocker):
    driver = MockDriver()
    driverif = StockBrockerDriverInterface(driver)
    driverif.login(ID, PW)
    return driverif, driver


def test_interface_creation(driver_interface_data):
    driver_interface, driver = driver_interface_data
    assert driver_interface is not None


def test_login(capsys, mocker):
    driver = MockDriver()
    driverif = StockBrockerDriverInterface(driver)
    try:
        driverif.login(ID, PW)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'login' in catured.out
    assert driver.login.called == 1

def test_login_fail(capsys, driver_interface_data):
    driver_interface, driver = driver_interface_data

    driver_interface.login(ID, PW)
    with pytest.raises(Exception):
        driver_interface.login(ID, PW)

    catured = capsys.readouterr()
    assert 'alreasy logined' in catured.out

    assert driver.login.called == 1

def test_get(driver_interface_data):
    driver_interface, driver = driver_interface_data

    driver.get_price.return_value = 1
    ret = driver_interface.get(STOCK)
    assert isinstance(ret, int)
    assert driver.get_price.called == 1


def test_buy(capsys, driver_interface_data):
    driver_interface, driver = driver_interface_data
    driver.buy.return_value =  print('Buy stock')
    try:
        driver_interface.buy(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'stock' in catured.out
    assert driver.buy.called == 1


def test_sell(capsys, driver_interface_data):
    driver_interface, driver = driver_interface_data
    driver.sell.return_value = print('Sell stock')

    try:
        driver_interface.sell(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'stock' in catured.out
    assert driver.sell.called == 1
