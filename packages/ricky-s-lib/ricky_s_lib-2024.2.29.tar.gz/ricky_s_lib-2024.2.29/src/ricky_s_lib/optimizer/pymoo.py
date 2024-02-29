from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import Problem
from pymoo.optimize import minimize as pymoo_minimize
from pymoo.visualization.scatter import Scatter

from ricky_s_lib.optimizer.utils import eval_func, get_info


def minimize(Params, func, pop_size):
    lower, upper, n_var, n_obj = get_info(Params, func)

    class MyProblem(Problem):
        def __init__(self):
            super().__init__(
                elementwise=True, n_var=n_var, n_obj=n_obj, xl=lower, xu=upper
            )

        def _evaluate(s, x, out):
            out["F"] = eval_func(Params, func, x)

    prob = MyProblem()
    algo = NSGA2(pop_size=pop_size)
    res = pymoo_minimize(problem=prob, algorithm=algo, seed=1, verbose=True)
    plot = Scatter()
    plot.add(res.F)
    plot.save("pareto_front.png")
