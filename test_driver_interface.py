import pytest
from pytest_mock import MockFixture


@pytest.fixture
def driver_interface(mocker):
    driver = mocker.Mock()
    return StockBrockerDriverInterface(driver), driver


def test_interface_creation(driver_interface_data):
    driver_interface, driver = driver_interface_data
    assert driver_interface is not None


def test_login(capsys, driver_interface_data):
    driver_interface, driver = driver_interface_data
    try:
        driver_interface.login()
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'login' in catured.out
    assert driver.login.called == 1


def test_get(driver_interface_data):
    driver_interface, driver = driver_interface_data
    interface = StockBrockerDriverInterface()
    ret = interface.get()
    assert isinstance(ret, int)
    assert driver.get.called == 1


def test_buy(capsys, driver_interface_data):
    driver_interface, driver = driver_interface_data
    interface = StockBrockerDriverInterface()
    try:
        interface.buy()
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'stock' in catured.out
    assert driver.buy.called == 1


def test_sell(capsys, driver_interface_data):
    driver_interface, driver = driver_interface_data
    interface = StockBrockerDriverInterface()
    try:
        interface.sell()
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'stock' in catured.out
    assert driver.sell.called == 1
