from jmetal.algorithm.multiobjective import NSGAII
from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution
from jmetal.lab.visualization import Plot
from jmetal.operator import PolynomialMutation, SBXCrossover
from jmetal.util.solution import get_non_dominated_solutions

from ricky_s_lib.optimizer.utils import eval_func, get_info


def minimize(Params, func, pop_size, dist_index=20):
    lower, upper, n_var, n_obj = get_info(Params, func)

    class Problem(FloatProblem):
        def __init__(s):
            super().__init__()
            s.lower_bound = lower
            s.upper_bound = upper
            s.directions = [s.MINIMIZE] * n_var

        def name(s):
            return "problem"

        def number_of_constraints(s):
            return 0

        def number_of_objectives(s):
            return n_obj

        def evaluate(s, sol: FloatSolution):
            sol.objectives = eval_func(Params, func, sol.variables)
            return sol

    prob = Problem()
    algo = NSGAII(
        problem=prob,
        population_size=pop_size,
        offspring_population_size=pop_size,
        mutation=PolynomialMutation(
            probability=1.0 / n_var,
            distribution_index=dist_index,
        ),
        crossover=SBXCrossover(
            probability=1.0,
            distribution_index=dist_index,
        ),
    )
    algo.run()
    front = get_non_dominated_solutions(algo.get_result())
    plot = Plot()
    plot.plot(front, filename="pareto_front", format="png")
