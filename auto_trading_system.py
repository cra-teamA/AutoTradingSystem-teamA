class AutoTradingSystem:
    def __init__(self):
        self._stock_brocker = None

    # 기본 기능
    def selectStockBrocker(self, stock_brocker):
        self._stock_brocker = stock_brocker

    def login(self, id):
        ...

    def buy(self, code, price, quantity): #refactor : interface에 추가
        ...

    def sell(self, code, price, quantity): #refactor : interface에 추가
        ...

    def getPrice(self, code):
        ...

    # 핵심 기능
    def getbuyNiceTiming(self, stock, price):
        ...

    def sellNiceTiming(self, quantity):
        ...