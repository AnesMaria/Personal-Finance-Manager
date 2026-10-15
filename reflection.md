# Reflection – Personal Finance Manager

<<<<<<< HEAD
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
=======
This project changed the way I look at design patterns. Before implementing them, they felt mostly like theoretical concepts with names and definitions. While building the finance manager, I started to see them as practical tools for solving very specific design problems.

I used four patterns in the project: Singleton, Adapter, Observer, and Strategy. What I found interesting is that each one improved a different part of the application rather than all solving the same kind of problem.

## Singleton Pattern

I used Singleton for the `Balance` class because I wanted the whole application to work with one shared balance.

This was important because having several independent balance objects would make the result confusing very quickly. A transaction could update one instance while another part of the application reads a different one.

One thing I noticed while testing this pattern is that shared state can easily stay between tests. I had to think about this more carefully than with a normal class. Adding a reset mechanism helped me make the tests predictable.

The downside is that Singleton introduces global state, which can become harder to manage in a bigger application. In this project, however, it matched the idea of one personal balance quite well.

## Adapter Pattern

The Adapter pattern made more sense to me once I worked with `ExternalFreelanceIncome`.

The external object had a different structure from the internal `Transaction` class. Instead of changing the external object or adding special cases everywhere, I used `TransactionAdapter` to translate it into the format the application already understands.

I liked this solution because the rest of the application does not need to care where the transaction came from.

The trade-off is that it adds another layer and another class. For a very small project, this can look like extra work, but I can see how it becomes useful when integrating several external systems.

## Observer Pattern

Observer was probably the pattern where the separation of responsibilities became the clearest to me.

The `Balance` class updates the financial state, but it does not need to know how the result should be displayed or when a warning should appear.

`PrintObserver` handles the balance display, while `LowBalanceAlertObserver` handles the low-balance condition.

A small design decision I had to make was deciding when the observers should be called. I chose to notify them only after the transaction has been applied successfully, so they always receive the current balance.

The main limitation is that when many observers are added, it can become less obvious what is triggered by one balance update. Good naming and tests become more important in that case.

## Strategy Pattern

For the fourth pattern, I chose Strategy because budgeting felt like a good example of behavior that can change without changing the rest of the application.

I implemented `FiftyThirtyTwentyStrategy` and `ZeroBasedBudgetStrategy`. The `BudgetPlanner` only knows that it has a strategy and that the strategy can create a budget.

What I liked here is that I could switch the budgeting method without rewriting the planner itself.

The part I had to think about was deciding where the responsibility should stop. I kept the planner simple and moved the actual allocation rules into each strategy.

The trade-off is that Strategy introduces more classes than a simple `if/else` block. For only two strategies, this may look heavier, but it makes adding a third or fourth budgeting rule much cleaner.

## Final Thoughts

The main thing I learned is that design patterns are useful when they answer a real design need.

In this project:

- Singleton kept one consistent balance.
- Adapter isolated an external transaction format.
- Observer separated balance changes from notifications.
- Strategy made budgeting behavior replaceable.

The project became a little more structured and had more classes than a very simple script would need, but the code also became easier to reason about and test.

If I continued working on it, I would add persistent storage for transactions and probably experiment with the Command pattern to support undoing a transaction.
>>>>>>> d36c9f5 (Update reflection, README, and fix PEP8 issues)
