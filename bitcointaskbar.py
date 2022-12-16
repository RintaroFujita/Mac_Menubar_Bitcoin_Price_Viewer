import ccxt
from pprint import pprint
import rumps

@rumps.timer(1)
def dispTimer(sender):
    coincheck = ccxt.coincheck()
    btc_price = coincheck.fetch_ticker(symbol="BTC/JPY")["last"]
    app.title = ("BitCoin: {}[円/BTC]".format(btc_price))
my_timer = rumps.Timer(dispTimer,1)
my_timer.start()


if __name__ == "__main__":
    app = rumps.App("Bit_Pri", title='Under measurement...')
    coincheck = ccxt.coincheck()


app.run()