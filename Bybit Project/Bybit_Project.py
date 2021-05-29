

import bybit
import time 


client= bybit.bybit(test=False,api_key="ap i_key", api_secret="api_secret")
print('loggedin')

info=client.Market.Market_symbolInfo().result()

keys=info[0]['result']
btc=keys[0]['last_price']
print(btc)

#Mark Price Request
import bybit

client = bybit.bybit(test=True, api_key="api_key", api_secret="api_secret")
print(client.LinearKline.LinearKline_markPrice(symbol="BTCUSDT", interval="m", limit=10, **{'from':1}).result())



# response

{
    "ret_code": 0,
    "ret_msg": "OK",
    "ext_code": "",
    "ext_info": "",
    "result": [{
        "id": 3866948,
        "symbol": "BTCUSDT",
        "period": "1",
        "start_at": 1577836800,
        "volume": 1451.59,
        "open": 7700,
        "high": 999999,
        "low": 0.5,
        "close": 6000
    },
    {
        "id": 3866948,
        "symbol": "BTCUSDT",
        "period": "1",
        "start_at": 1577836800,
        "volume": 1451.59,
        "open": 7700,
        "high": 999999,
        "low": 0.5,
        "close": 6000
    }],
    "time_now": "1581928016.558522"
}

# Place anActive Order
import bybit
client = bybit.bybit(test=True, api_key="api_key", api_secret="api_secret")
print(client.LinearOrder.LinearOrder_new(side="Sell",symbol="BTCUSDT",order_type="Limit",qty=0.22,price=10000,time_in_force="GoodTillCancel",reduce_only=False, close_on_trigger=False).result())

{
    "ret_code": 0,
    "ret_msg": "OK",
    "ext_code": "",
    "ext_info": "",
    "result": {
        "order_id":"bd1844f-f3c0-4e10-8c25-10fea03763f6",
        "user_id": 1,
        "symbol": "BTCUSDT",
        "side": "Sell",
        "order_type": "Limit",
        "price": 8083,
        "qty": 10,
        "time_in_force": "GoodTillCancel",
        "order_status": "New",
        "last_exec_price": 8083,       #Last execution price
        "cum_exec_qty": 0,             #Cumulative qty of trading
        "cum_exec_value": 0,           #Cumulative value of trading
        "cum_exec_fee": 0,             #Cumulative trading fees
        #"reduce_only": false,          #true means close order, false means open position
        #"close_on_trigger": false,
        "order_link_id": " ",
        "created_time": "2019-10-21T07:28:19.396246Z",
        "updated_time": "2019-10-21T07:28:19.396246Z",
    },
    "time_now": "1575111823.458705",
    "rate_limit_status": 98,
    "rate_limit_reset_ms": 1580885703683,
    "rate_limit": 100
}