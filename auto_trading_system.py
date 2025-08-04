from time import sleep

from driver_mock import MockDriver

class AutoTradingSystem:
    def __init__(self):
        self._stock_brocker = None

    # 기본 기능
    def selectStockBrocker(self, stock_brocker):
        self._stock_brocker = stock_brocker

    def login(self, id, password):
        self._stock_brocker.login(id, password)

    def buy(self, stock, price, quantity):
        self._stock_brocker.buy(stock, price, quantity)

    def sell(self, stock, price, count):
        self._stock_brocker.sell(stock, price, count)

    def getPrice(self, stock):
        return self._stock_brocker.get(stock)

    def getbuyNiceTiming(self, stock, price):
        price1 = self._stock_brocker.get(stock)
        sleep(200/1000)
        price2 = self._stock_brocker.get(stock)
        sleep(200/1000)
        price3 = self._stock_brocker.get(stock)
        if not (price1 < price2 < price3):
            raise Exception()
        else:
            count = price // price3
            return self._stock_brocker.buy(stock, count, price3)

    def sellNiceTiming(self, stock, count):
        price1 = self._stock_brocker.get(stock)
        sleep(200/1000)
        price2 = self._stock_brocker.get(stock)
        sleep(200/1000)
        price3 = self._stock_brocker.get(stock)
        if not(price1 > price2 > price3):
            raise Exception()
        else:
            return self._stock_brocker.sell(stock, count, price3)
