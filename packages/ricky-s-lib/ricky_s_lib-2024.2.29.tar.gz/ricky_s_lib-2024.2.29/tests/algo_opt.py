import numpy as np
import talib as ta

from ricky_s_lib.optimizer.pymoo import minimize
from ricky_s_lib.optimizer.Recorder import Recorder
from ricky_s_lib.optimizer.utils import to_dict
from ricky_s_lib.trading.analyze import analyze
from ricky_s_lib.trading.data import load_data
from ricky_s_lib.trading.sim import ENTER, EXIT, sim

path = r"D:\data\crypto\USDT_5m_2022-08-01_2023-08-01.pkl"
data = load_data(path, 0, 1)
recorder = Recorder()
best = None


class Params:
    ma_period = [30, 10, 90, 0]
    high_offset = [1.03, 1.01, 1.09, 3]
    low_offset = [0.99, 0.95, 1.0, 3]
    # n_slot = [5, 3, 10]
    # leverage = [2, 1, 5]
    take_profit = [0.02, 0.01, 0.05, 3]
    stop_loss = [-0.2, -0.5, -0.1, 2]
    timeout = [360, 100, 600, 0]


def func(pa: Params):
    def algo(o, h, l, c, v, long, short):
        ma = ta.KAMA(c, int(pa.ma_period))
        short[c > ma * pa.high_offset] = ENTER
        short[c < ma * pa.low_offset] = EXIT

    conf = {
        "n_slot": 5,
        "leverage": 2,
        "take_profit": pa.take_profit,
        "stop_loss": pa.stop_loss,
        "timeout": pa.timeout,
        "fee": 0.0005,
    }

    hist, trades = sim(data, algo, conf)
    worth, dd = hist[:, 2], hist[:, 3]
    max_worth, min_dd, mean_dd = worth.max(), dd.min(), dd.mean()
    global best
    if best is None or max_worth > best:
        best = max_worth
        analyze(hist, trades)
    log_max_worth = np.log10(max_worth)
    recorder.add(
        x=to_dict(pa),
        y=[log_max_worth, min_dd, mean_dd],
        labels=["log_max_worth", "min_dd", "mean_dd"],
        sort=lambda y: -y[0],
    )
    return [-log_max_worth, -min_dd, -mean_dd]


minimize(Params, func, pop_size=100)
