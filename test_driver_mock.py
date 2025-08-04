import pytest
from driver_mock import MockDriver, MockIncreasingDriver, MockDecreasingDriver

ID = 'id'
PW = 'pw'
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000

def test_interface_creation():
    interface = MockDriver()

    assert interface is not None
def test_login(capsys):
    interface = MockDriver()
    try:
        interface.login(ID, PW)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'login success' in catured.out

def test_get():
    interface = MockDriver()
    ret = interface.get_price(STOCK)
    assert isinstance(ret, int)

def test_buy(capsys):
    interface = MockDriver()
    try:
        interface.buy(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'success to purchase' in catured.out

def test_sell(capsys):
    interface = MockDriver()
    try:
        interface.sell(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'success to sell' in catured.out
def test_get_increased_price():
    interface = MockIncreasingDriver()
    ret1 = interface.get_price(STOCK)
    ret2 = interface.get_price(STOCK)
    ret3 = interface.get_price(STOCK)
    assert isinstance(ret1, int) and isinstance(ret2, int) and isinstance(ret3, int)
    assert ret1 < ret2
    assert ret2 < ret3

def test_get_decreased_price():
    interface = MockDecreasingDriver()
    ret1 = interface.get_price(STOCK)
    ret2 = interface.get_price(STOCK)
    ret3 = interface.get_price(STOCK)
    assert isinstance(ret1, int) and isinstance(ret2, int) and isinstance(ret3, int)
    assert ret1 > ret2
    assert ret2 > ret3
