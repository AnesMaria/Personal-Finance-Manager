# Personal Finance Manager

## Project Overview

This project is a small personal finance manager built in Python.

The application allows users to:

- track income and expenses;
- maintain a single shared balance;
- convert external transactions into the internal transaction format;
- receive notifications when the balance changes;
- trigger alerts when the balance falls below a defined threshold;
- apply different budgeting strategies.

The main objective of the project was to practice object-oriented programming
and understand how design patterns can make a small application easier to
maintain, test, and extend.

---

## Design Patterns Used

This project uses four design patterns:

- Singleton Pattern
- Adapter Pattern
- Observer Pattern
- Strategy Pattern

Each pattern solves a different design problem in the application.

---

## Singleton Pattern

The `Balance` class uses the Singleton pattern.

I used this pattern because the application should only have one shared
financial balance. If several balance objects were created independently,
transactions could update different values and the application could become
inconsistent.

Using a Singleton ensures that every part of the program works with the same
balance instance.

One challenge with this pattern was testing shared state because the same
instance can remain between tests. I addressed this by using a reset mechanism
so that each test can start from a predictable state.

The main trade-off is that Singleton introduces global shared state, which can
become more difficult to manage in a larger application. For this project,
however, one shared balance matches the problem well.

---

## Adapter Pattern

The Adapter pattern is used for external freelance income.

The external income object does not have the same structure as the internal
`Transaction` class. Instead of changing the transaction model or adding
special cases throughout the application, I used `TransactionAdapter` to
convert the external object into a standard transaction.

This keeps the rest of the application independent of the external format and
makes it easier to support additional external transaction sources later.

The trade-off is that the Adapter introduces another class and another layer
of abstraction. For a very small application this may seem unnecessary, but
it prevents external formats from becoming tightly coupled to the core
transaction logic.

---

## Observer Pattern

The Observer pattern is used to react to balance changes.

The application contains two observers:

- `PrintObserver`, which displays the updated balance after a transaction;
- `LowBalanceAlertObserver`, which triggers an alert when the balance falls
  below a defined threshold.

What I found useful about this pattern is that the `Balance` class does not
need to know how each notification works. It only notifies registered
observers after a successful balance update.

This makes it possible to add more notification behaviors later without
changing the balance calculation logic.

A design decision I had to make was deciding when observers should be
notified. I chose to notify them only after the transaction has been applied
successfully so that they always receive the updated balance.

The trade-off is that event-driven behavior can become harder to follow when
many observers are registered.

---

## Strategy Pattern

For the fourth pattern, I chose the Strategy pattern.

I used it for budget planning because different users may want to manage their
money using different budgeting rules.

The project currently includes:

- `FiftyThirtyTwentyStrategy`
- `ZeroBasedBudgetStrategy`

The `BudgetPlanner` can switch between strategies without changing its own
implementation.

I chose this pattern because budgeting rules are behaviors that can vary
independently from the rest of the application. A new budgeting strategy can
be added without modifying the planner.

One challenge was deciding which responsibility belonged to the planner and
which belonged to the strategy. I kept the planner responsible only for
selecting and calling a strategy, while each strategy contains its own
allocation logic.

The trade-off is that Strategy introduces more classes than a simple
conditional statement would require. In return, the budgeting rules are
isolated, easier to test, and easier to extend.

---

## Project Structure

```text
.
├── balance/
│   ├── __init__.py
│   ├── balance.py
│   ├── balance_observer.py
│   ├── test_balance.py
│   └── test_balance_observer.py
│
├── transaction/
│   ├── __init__.py
│   ├── transaction.py
│   ├── transaction_category.py
│   ├── transaction_adapter.py
│   ├── external_income_transaction.py
│   ├── test_transaction.py
│   └── test_transaction_adapter.py
│
├── budget/
│   ├── __init__.py
│   ├── budget_strategy.py
│   └── test_budget_strategy.py
│
├── main.py
├── reflection.md
└── README.md
```

---

## Running the Application

From the project root, run:

```bash
python main.py
```

The application:

- creates the shared balance;
- registers the observers;
- processes income and expense transactions;
- adapts an external freelance income;
- displays balance updates;
- demonstrates the two budgeting strategies.

---

## Running the Tests

Run all unit tests with:

```bash
python -m unittest discover -v
```

The project currently contains 17 passing tests.

The tests cover:

- balance management;
- Singleton behavior;
- transaction creation;
- transaction equality and representation;
- Adapter behavior;
- Observer behavior;
- Strategy behavior.

---

## Code Quality

The project follows PEP8 formatting conventions.

To check the code style, run:

```bash
python -m pycodestyle balance budget transaction main.py
```

A successful style check produces no output.

The project was also verified by running the full test suite after formatting
changes to make sure that code style corrections did not affect behavior.

---

## Reflection

Working on this project helped me move from understanding design patterns as
theoretical concepts to seeing where they are actually useful in code.

The four patterns solve different problems in the application:

- Singleton keeps one consistent shared balance.
- Adapter isolates external transaction formats.
- Observer separates balance management from notifications.
- Strategy allows budgeting behavior to be changed independently.

The patterns add more classes than a very simple finance script would need,
but they also make the responsibilities clearer and easier to test.

A more detailed discussion of the design decisions, challenges, and trade-offs
for each pattern is available in:

[`reflection.md`](reflection.md)

---

## Possible Future Improvements

If I continued this project, I would consider adding:

- persistent transaction storage;
- stronger input validation;
- more budgeting strategies;
- logging;
- a command history;
- undo/redo support using the Command pattern.

---

## Final Verification

Before submission, I verified that:

```bash
python -m unittest discover -v
```

passes all tests, and:

```bash
python -m pycodestyle balance budget transaction main.py
```

reports no style errors.

The project is organized into separate modules for balance management,
transactions, budgeting strategies, and tests.