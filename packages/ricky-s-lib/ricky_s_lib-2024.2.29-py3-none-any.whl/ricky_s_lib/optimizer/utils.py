import numpy as np


class Params:
    pass


def to_dict(x: Params):
    return {k: v for k, v in x.__dict__.items() if not k.startswith("__")}


def get_info(Params: Params, func):
    dic = to_dict(Params)
    lower = np.array([v[1] for v in dic.values()])
    upper = np.array([v[2] for v in dic.values()])
    assert np.all(upper > lower)

    pa = Params()
    for k, v in dic.items():
        setattr(pa, k, v[0])
    n_var = len(dic)
    n_obj = len(func(pa))
    return lower, upper, n_var, n_obj


def eval_func(Params: Params, func, x):
    dic = to_dict(Params)
    pa = Params()
    for i, (k, v) in enumerate(dic.items()):
        setattr(pa, k, round(x[i], v[3]))
    return func(pa)
