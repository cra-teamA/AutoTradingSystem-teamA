import pytest

ID = 'id'
PW = 'pw'
STOCK = 'SAMSUNG'
COUNT = 1
PRICE = 100000

def test_interface_creation():
    interface = DriverMock()

    assert interface is not None
def test_login(capsys):
    interface = DriverMock()
    try:
        interface.login(ID, PW)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'login success' in catured.out
def test_get():
    interface = DriverMock()
    ret = interface.get(STOCK)
    assert isinstance(ret, int)
def test_buy(capsys):
    interface = DriverMock()
    try:
        interface.buy(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'success to purchase' in catured.out
def test_sell(capsys):
    interface = DriverMock()
    try:
        interface.sell(STOCK, COUNT, PRICE)
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'success to sell' in catured.out