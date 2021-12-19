from typing import Sized


class TradeData:
    symbol: str = ''
    datatime: str = ''
    direction: str = ''
    price: float = 0.0
    volume: float = 0.0
    size: int = 0
    def __init__(
        self,
        symbol: str,
        datatime: str,
        direction: str,
        price: float,
        volume: float,
        size: int
    ):
        self.symbol = symbol
        self.datatime = datatime
        self.price = price
        self.volume = volume
        self.direction = direction
        self.size = size
    def calculate_trading_value(self, size:int) -> float:
        '''计算成交金额的对象方法'''
        value = self.price * self.volume * self.size
        return value
    def to_str(self)->str:
        text = f'{self.datatime}{self.direction}{self.symbol}{self.volume}手@{self.price}'
        return text
class StockTradeData(TradeData):

    def calculate_cash_change(self):
        '''计算股票现金变化'''
        value = self.price * self.volume * self.size    

stock_trade = StockTradeData(
    '600036','20211226','买入',40,100,1
)
print(stock_trade.to_str())