class StockBrockerDriverInterface:
    def __init__(self, driver):
        self._driver = driver
        self._is_logined = False

    def login(self, id, pw):
        if self._is_logined:
            print("already logined")
            raise Exception()
        self._driver.login(id, pw)
        self._is_logined = True
        print('login')


    def get(self, stock):
        return self._driver.get(stock)

    def buy(self, stock, count, price):
        return self._driver.buy(stock, count, price)

    def sell(self, stock, count, price):
        return self._driver.sell(stock, count, price)




