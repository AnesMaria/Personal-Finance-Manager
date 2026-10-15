import unittest

from budget.budget_strategy import (
    BudgetPlanner,
    FiftyThirtyTwentyStrategy,
    ZeroBasedBudgetStrategy,
)


class TestBudgetStrategy(unittest.TestCase):

    def test_fifty_thirty_twenty_strategy(self):
        planner = BudgetPlanner(FiftyThirtyTwentyStrategy())

        budget = planner.create_budget(1000)

        self.assertEqual(budget["needs"], 500.0)
        self.assertEqual(budget["wants"], 300.0)
        self.assertEqual(budget["savings"], 200.0)

    def test_zero_based_budget_strategy(self):
        planner = BudgetPlanner(ZeroBasedBudgetStrategy())

        budget = planner.create_budget(1000)

        self.assertEqual(budget["assigned"], 1000)
        self.assertEqual(budget["unallocated"], 0)

    def test_strategy_can_be_changed(self):
        planner = BudgetPlanner(FiftyThirtyTwentyStrategy())

        budget1 = planner.create_budget(1000)
        self.assertEqual(budget1["savings"], 200.0)

        planner.set_strategy(ZeroBasedBudgetStrategy())

        budget2 = planner.create_budget(1000)
        self.assertEqual(budget2["assigned"], 1000)

    def test_negative_income_raises_error(self):
        planner = BudgetPlanner(FiftyThirtyTwentyStrategy())

        with self.assertRaises(ValueError):
            planner.create_budget(-100)


if __name__ == "__main__":
    unittest.main()