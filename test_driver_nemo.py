import pytest
from driver_mock import MockDriver
from nemo_driver import NemoDriver

ID = 'id'
PW = 'pw'
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000

def test_interface_creation():
    interface = NemoDriver()

    assert interface is not None
def test_login(capsys):
    interface = NemoDriver()
    try:
        interface.login(ID, PW)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'login success' in catured.out

def test_get():
    interface = NemoDriver()
    ret = interface.get_price(STOCK)
    assert isinstance(ret, int)

def test_buy(capsys):
    interface = NemoDriver()
    try:
        interface.buy(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'success to purchase' in catured.out

def test_sell(capsys):
    interface = NemoDriver()
    try:
        interface.sell(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'success to sell' in catured.out
