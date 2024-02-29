import talib as ta

from ricky_s_lib.trading.analyze import analyze
from ricky_s_lib.trading.data import load_data
from ricky_s_lib.trading.sim import ENTER, EXIT, sim

path = r"D:\data\crypto\USDT_5m_2022-08-01_2023-08-01.pkl"
# path = r"D:\data\crypto\USDT_5m_2023-06-01_2023-07-01.pkl"
data = load_data(path, 0, 1)


def algo(o, h, l, c, v, long, short):
    ma = ta.KAMA(c, 28)
    # long[c < ma * 0.96] = ENTER
    # long[c > ma * 1.01] = EXIT
    short[c > ma * 1.03] = ENTER
    short[c < ma * 0.99] = EXIT


conf = {
    "n_slot": 5,
    "leverage": 2,
    "take_profit": 0.02,
    "stop_loss": -0.2,
    "timeout": 360,
    "fee": 0.0005,
}

hist, trades = sim(data, algo, conf)
analyze(hist, trades)
