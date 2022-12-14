import logging

import MetaTrader5 as mt5

from order import Order


def make_order(order: Order, lot=0.1, tp_number=1):
    if not mt5.initialize():
        logging.error('Problem with initialize')
        return False
    symbol = order.get_symbol()
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        logging.error('Problem with symbol_info')
        mt5.shutdown()
        return False
    if not symbol_info.visible:
        if not mt5.symbol_select(symbol, True):
            logging.error('Problem with symbol_info.visible')
            mt5.shutdown()
            return False
    if order.get_type() == 'BUY':
        price = mt5.symbol_info_tick(symbol).ask
        order_type = mt5.ORDER_TYPE_BUY
    else:
        price = mt5.symbol_info_tick(symbol).bid
        order_type = mt5.ORDER_TYPE_SELL
    take_profit = order.get_take_profit1() if tp_number == 1 else order.get_take_profit2()
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type":  order_type,
        "price": price,
        "sl": order.get_stop_loss(),
        "tp": take_profit,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": 0,
    }
    mt5.order_send(request)
    logging.info('Sent')
    mt5.shutdown()
    return True
