# Reflection – Personal Finance Manager

This project helped me understand why design patterns are useful beyond their
theoretical definitions. I implemented four patterns: Singleton, Adapter,
Observer, and Strategy. Each one solved a different design problem in the
application.

## Singleton Pattern

I used the Singleton pattern for the `Balance` class because the application
should have only one shared financial balance. If different parts of the
program could create independent balance objects, transactions could be
applied to different balances and the result would become inconsistent.

The Singleton made the shared state explicit and also made it easy for the
different parts of the application to access the same balance.

One difficulty I encountered was testing a Singleton because its state can
remain between tests. I addressed this by adding a reset mechanism so that
each test can start with a known balance.

The trade-off is that Singleton introduces global shared state, which can make
larger applications harder to test or extend. For this small application,
however, having one shared balance matched the problem well.

## Adapter Pattern

I used the Adapter pattern because `ExternalFreelanceIncome` does not use the
same interface as the application's internal `Transaction` class.

Instead of modifying the external object or adding special cases throughout
the finance manager, `TransactionAdapter` converts the external freelance
income into a standard `Transaction`.

This keeps the rest of the application independent of the external format.
It also makes the code easier to extend because another external transaction
format could later have its own adapter.

The main trade-off is that the Adapter adds another class to the project.
For a small application this may seem unnecessary, but it prevents external
data formats from becoming coupled to the core transaction logic.

## Observer Pattern

I used the Observer pattern for balance notifications. The `Balance` class
notifies registered observers whenever a transaction changes the balance.

`PrintObserver` displays the new balance, while
`LowBalanceAlertObserver` checks whether the balance has fallen below a
configured threshold.

The main benefit is separation of responsibilities. The `Balance` class only
manages the financial state and does not need to contain printing or alert
logic. New notification behaviors could be introduced later without changing
the balance calculation.

A challenge was deciding when observers should be notified. I chose to notify
them only after the transaction has been successfully applied so that they
always receive the updated balance.

The trade-off is that event-driven behavior can be less obvious to follow than
a direct method call, especially when several observers are registered.

## Strategy Pattern

For the fourth pattern, I chose Strategy for budget planning. I implemented a
`FiftyThirtyTwentyStrategy` and a `ZeroBasedBudgetStrategy`.

I chose Strategy because budgeting rules are behaviors that may vary from one
user or situation to another. The `BudgetPlanner` does not need to know the
details of each budgeting algorithm. It delegates the calculation to the
currently selected strategy.

This improves flexibility because a strategy can be changed at runtime and a
new budgeting method can be added without modifying `BudgetPlanner`.

One challenge was deciding what should belong to the strategy and what should
remain in the planner. I kept the planner responsible only for selecting and
calling a strategy, while each strategy contains its own allocation logic.

The trade-off is that Strategy creates more classes than a simple conditional
statement would require. I think this is worthwhile here because it keeps the
budgeting algorithms isolated and independently testable.

## Final Thoughts

The biggest lesson from this project was that design patterns should solve a
specific design problem rather than be added only because they are available.

Singleton gave the application one consistent balance, Adapter isolated an
external transaction format, Observer separated notifications from balance
management, and Strategy made budgeting behavior replaceable.

The patterns increased the number of classes in the project, but they also
made each class more focused and made the application easier to test and
extend. If I continued the project, I would add persistent transaction
storage and possibly use the Command pattern to support undoing transactions.
