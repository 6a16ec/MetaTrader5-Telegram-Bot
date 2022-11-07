import MetaTrader5 as mt5


class Mt5:
    def __init__(self):
        mt5.initialize()
        self.__symbol = None

    def set_symbol(self, symbol):
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info:
            if not symbol_info.visible:
                mt5.symbol_select(symbol, True)
            self.__symbol = symbol

    def make_order(self, lot, sl, tp):
        price = mt5.symbol_info_tick(self.__symbol).ask
        deviation = 20
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.__symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        mt5.order_send(request)

    def __del__(self):
        mt5.shutdown()


if __name__ == '__main__':
    mt5 = Mt5()
    mt5.set_symbol('GBPJPY')
    mt5.make_order(lot=1, sl=170, tp=165)

# send a trading request
# check the execution result
# print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation));
# if result.retcode != mt5.TRADE_RETCODE_DONE:
#     print("2. order_send failed, retcode={}".format(result.retcode))
#     # request the result as a dictionary and display it element by element
#     result_dict = result._asdict()
#     for field in result_dict.keys():
#         print("   {}={}".format(field, result_dict[field]))
#         # if this is a trading request structure, display it element by element as well
#         if field == "request":
#             traderequest_dict = result_dict[field]._asdict()
#             for tradereq_filed in traderequest_dict:
#                 print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
#     print("shutdown() and quit")
#     mt5.shutdown()
#     quit()
#
# print("2. order_send done, ", result)
# print("   opened position with POSITION_TICKET={}".format(result.order))
# print("   sleep 2 seconds before closing position #{}".format(result.order))
# time.sleep(2)
# # create a close request
# position_id = result.order
# price = mt5.symbol_info_tick(symbol).bid
# deviation = 20
# request = {
#     "action": mt5.TRADE_ACTION_DEAL,
#     "symbol": symbol,
#     "volume": lot,
#     "type": mt5.ORDER_TYPE_SELL,
#     "position": position_id,
#     "price": price,
#     "deviation": deviation,
#     "magic": 234000,
#     "comment": "python script close",
#     "type_time": mt5.ORDER_TIME_GTC,
#     "type_filling": mt5.ORDER_FILLING_RETURN,
# }
# # send a trading request
# result = mt5.order_send(request)
# # check the execution result
# print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id, symbol, lot, price,
#                                                                                      deviation));
# if result.retcode != mt5.TRADE_RETCODE_DONE:
#     print("4. order_send failed, retcode={}".format(result.retcode))
#     print("   result", result)
# else:
#     print("4. position #{} closed, {}".format(position_id, result))
#     # request the result as a dictionary and display it element by element
#     result_dict = result._asdict()
#     for field in result_dict.keys():
#         print("   {}={}".format(field, result_dict[field]))
#         # if this is a trading request structure, display it element by element as well
#         if field == "request":
#             traderequest_dict = result_dict[field]._asdict()
#             for tradereq_filed in traderequest_dict:
#                 print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
#
# # shut down connection to the MetaTrader 5 terminal
# mt5.shutdown()
