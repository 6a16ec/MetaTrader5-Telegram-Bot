import re

symbol_replacement = {'GOLD': 'XAUUSD'}


class Order:
    def __init__(self, text: str):
        self.__text = text.upper()
        self.__words = self.__text.split()
        self.__symbol = self.__parse_symbol()
        self.__type = self.__parse_type()
        self.__stop_loss = self.__parse_stop_loss()
        self.__take_profit1 = self.__parse_take_profit1()
        self.__take_profit2 = self.__parse_take_profit2()

    def __parse_symbol(self):
        symbol = None
        if len(self.__words) > 0:
            symbol = self.__words[0]
        for symbol_was, symbol_new in symbol_replacement.items():
            if symbol == symbol_was:
                symbol = symbol_new
        return symbol

    def __parse_type(self):
        order_type = None
        if 'BUY' in self.__words:
            order_type = 'BUY'
        elif 'SELL' in self.__words:
            order_type = 'SELL'
        return order_type

    def __parse_stop_loss(self):
        stop_loss = None
        result = re.findall(r"SL:?\s*(\d+\.?\d+)", self.__text)
        if result:
            stop_loss = float(result[0])
        return stop_loss

    def __parse_take_profit1(self):
        take_profit1 = None
        result = re.findall(r"TP1:?\s*(\d+\.?\d+)", self.__text)
        if result:
            take_profit1 = float(result[0])
        return take_profit1

    def __parse_take_profit2(self):
        take_profit2 = None
        result = re.findall(r"TP2:?\s*(\d+\.?\d+)", self.__text)
        if result:
            take_profit2 = float(result[0])
        return take_profit2

    def is_valid(self):
        return self.__symbol is not None and \
               self.__type is not None and \
               self.__stop_loss is not None and \
               self.__take_profit1 is not None and \
               self.__take_profit2 is not None

    def get_symbol(self):
        return self.__symbol

    def get_type(self):
        return self.__type

    def get_stop_loss(self):
        return self.__stop_loss

    def get_take_profit1(self):
        return self.__take_profit1

    def get_take_profit2(self):
        return self.__take_profit2
