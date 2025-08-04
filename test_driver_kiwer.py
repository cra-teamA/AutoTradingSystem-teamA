import pytest
from driver_kiwer import KiwerDriver

ID = 'id'
PW = 'pw'
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000

def test_interface_creation():
    interface = KiwerDriver()
    assert interface is not None

def test_login(capsys):
    interface = KiwerDriver()
    interface.login(ID, PW)
    catured = capsys.readouterr()
    assert f'{ID} login success' in catured.out

def test_get():
    interface = KiwerDriver()
    ret = interface.get_price(STOCK)
    assert isinstance(ret, int)


def test_buy(capsys):
    interface = KiwerDriver()
    try:
        interface.buy(STOCK, PRICE, COUNT)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert f'{STOCK} : Buy stock ( {PRICE} * {COUNT}\n' == catured.out


def test_sell(capsys):
    interface = KiwerDriver()
    try:
        interface.sell(STOCK, PRICE, COUNT)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert f'{STOCK} : Sell stock ( {PRICE} * {COUNT}\n' == catured.out
