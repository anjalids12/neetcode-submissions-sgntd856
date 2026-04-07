class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        mininmizer = init
        for i in range(iterations):
            der_cost_func = 2*mininmizer
            mininmizer = mininmizer - learning_rate*der_cost_func
        return round(mininmizer,5)
