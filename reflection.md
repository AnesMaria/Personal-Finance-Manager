# Reflection – Personal Finance Manager

This project changed the way I look at design patterns. Before implementing
them, they felt mostly like theoretical concepts with names and definitions.
While building the finance manager, I started to see them as practical tools
for solving very specific design problems.

I used four patterns in the project: Singleton, Adapter, Observer, and
Strategy. What I found interesting is that each one improved a different part
of the application rather than all solving the same kind of problem.

## Singleton Pattern

I used Singleton for the `Balance` class because I wanted the whole
application to work with one shared balance.

This was important because having several independent balance objects would
make the result confusing very quickly. A transaction could update one
instance while another part of the application reads a different one.

One thing I noticed while testing this pattern is that shared state can easily
stay between tests. I had to think about this more carefully than with a normal
class. Adding a reset mechanism helped me make the tests predictable.

The downside is that Singleton introduces global state, which can become harder
to manage in a bigger application. In this project, however, it matched the
idea of one personal balance quite well.

## Adapter Pattern

The Adapter pattern made more sense to me once I worked with
`ExternalFreelanceIncome`.

The external object had a different structure from the internal `Transaction`
class. Instead of changing the external object or adding special cases
everywhere, I used `TransactionAdapter` to translate it into the format the
application already understands.

I liked this solution because the rest of the application does not need to
care where the transaction came from.

The trade-off is that it adds another layer and another class. For a very
small project, this can look like extra work, but I can see how it becomes
useful when integrating several external systems.

## Observer Pattern

Observer was probably the pattern where the separation of responsibilities
became the clearest to me.

The `Balance` class updates the financial state, but it does not need to know
how the result should be displayed or when a warning should appear.

`PrintObserver` handles the balance display, while `LowBalanceAlertObserver`
handles the low-balance condition.

A small design decision I had to make was deciding when the observers should
be called. I chose to notify them only after the transaction has been applied
successfully, so they always receive the current balance.

The main limitation is that when many observers are added, it can become less
obvious what is triggered by one balance update. Good naming and tests become
more important in that case.

## Strategy Pattern

For the fourth pattern, I chose Strategy because budgeting felt like a good
example of behavior that can change without changing the rest of the
application.

I implemented `FiftyThirtyTwentyStrategy` and
`ZeroBasedBudgetStrategy`. The `BudgetPlanner` only knows that it has a
strategy and that the strategy can create a budget.

What I liked here is that I could switch the budgeting method without
rewriting the planner itself.

The part I had to think about was deciding where the responsibility should
stop. I kept the planner simple and moved the actual allocation rules into
each strategy.

The trade-off is that Strategy introduces more classes than a simple
`if/else` block. For only two strategies, this may look heavier, but it makes
adding a third or fourth budgeting rule much cleaner.

## Final Thoughts

The main thing I learned is that design patterns are useful when they answer a
real design need.

In this project:

- Singleton kept one consistent balance.
- Adapter isolated an external transaction format.
- Observer separated balance changes from notifications.
- Strategy made budgeting behavior replaceable.

The project became a little more structured and had more classes than a very
simple script would need, but the code also became easier to reason about and
test.

If I continued working on it, I would add persistent storage for transactions
and probably experiment with the Command pattern to support undoing a
transaction.
