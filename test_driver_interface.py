import pytest


def test_interface_creation():
    interface = StockBrockerDriverInterface()

    assert interface is not None
def test_login(capsys):
    interface = StockBrockerDriverInterface()
    try:
        interface.login()
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'login' in catured.out
def test_get():
    interface = StockBrockerDriverInterface()
    ret = interface.get()
    assert isinstance(ret, int)
def test_buy(capsys):
    interface = StockBrockerDriverInterface()
    try:
        interface.buy()
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'stock' in catured.out
def test_sell(capsys):
    interface = StockBrockerDriverInterface()
    try:
        interface.sell()
    except:
        pytest.fail()
    catured = capsys.readouterr()
    assert 'stock' in catured.out