"""Hart-Mas-Colell Regret Matching Learning Dynamics.
100% Python Standard Library.
"""

class RegretMatchingLearner:
    """Online no-regret learning agent converging to set of correlated equilibria."""
    def __init__(self, num_actions):
        self.num_actions = num_actions
        self.regret_sum = [0.0] * num_actions
        self.strategy_sum = [0.0] * num_actions

    def get_strategy(self):
        positive_regrets = [max(r, 0.0) for r in self.regret_sum]
        total = sum(positive_regrets)
        if total > 1e-8:
            return [r / total for r in positive_regrets]
        return [1.0 / self.num_actions] * self.num_actions

    def update(self, action_taken, payoffs):
        actual_payoff = payoffs[action_taken]
        for a in range(self.num_actions):
            self.regret_sum[a] += (payoffs[a] - actual_payoff)
            
        strat = self.get_strategy()
        for a in range(self.num_actions):
            self.strategy_sum[a] += strat[a]

    def get_average_strategy(self):
        total = sum(self.strategy_sum)
        if total > 1e-8:
            return [round(s / total, 4) for s in self.strategy_sum]
        return [round(1.0 / self.num_actions, 4)] * self.num_actions
