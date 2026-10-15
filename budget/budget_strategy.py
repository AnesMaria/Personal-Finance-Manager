from abc import ABC, abstractmethod


class BudgetStrategy(ABC):
    """
    Base strategy interface for budget allocation.
    """

    @abstractmethod
    def allocate(self, income):
        """
        Return a dictionary describing how income should be allocated.
        """
        pass


class FiftyThirtyTwentyStrategy(BudgetStrategy):
    """
    50/30/20 budgeting strategy:
    - 50% needs
    - 30% wants
    - 20% savings
    """

    def allocate(self, income):
        if income < 0:
            raise ValueError("Income must be non-negative.")

        return {
            "needs": income * 0.50,
            "wants": income * 0.30,
            "savings": income * 0.20,
        }


class ZeroBasedBudgetStrategy(BudgetStrategy):
    """
    Simple zero-based budgeting strategy.
    For this project, all income is intentionally assigned.
    """

    def allocate(self, income):
        if income < 0:
            raise ValueError("Income must be non-negative.")

        return {
            "assigned": income,
            "unallocated": 0,
        }


class BudgetPlanner:
    """
    Context class that uses a selected budget strategy.
    """

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def create_budget(self, income):
        return self.strategy.allocate(income)