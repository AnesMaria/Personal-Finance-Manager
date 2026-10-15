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

The main objective of the project was to practice object-oriented programming and understand how design patterns can make a small application easier to maintain and extend.

---

## Design Patterns Used

This project uses four design patterns:

- Singleton Pattern
- Adapter Pattern
- Observer Pattern
- Strategy Pattern

Each pattern solves a different problem in the application.

---

## Singleton Pattern

The `Balance` class uses the Singleton pattern.

I used this pattern because the application should only have one shared balance. If several balance objects were created independently, transactions could update different values and the application would quickly become inconsistent.

Using a Singleton ensures that every part of the program works with the same balance instance.

---

## Adapter Pattern

The Adapter pattern is used for external freelance income.

The external income object does not have the same structure as the internal `Transaction` class. Instead of changing the transaction model, I used `TransactionAdapter` to convert the external object into a standard transaction.

I found this pattern useful because it keeps external formats separate from the core application logic.

---

## Observer Pattern

The Observer pattern is used to react to balance changes.

The application contains two observers:

- `PrintObserver`, which displays the balance after a transaction;
- `LowBalanceAlertObserver`, which triggers an alert when the balance becomes too low.

What I liked about this pattern is that the `Balance` class does not need to know exactly what each observer does. It only sends notifications when something changes.

This makes it easier to add more notifications later without changing the balance logic.

---

## Strategy Pattern

For the fourth pattern, I chose the Strategy pattern.

I used it for budget planning because different users may want to manage their money in different ways.

The project currently includes:

- `FiftyThirtyTwentyStrategy`
- `ZeroBasedBudgetStrategy`

The `BudgetPlanner` can switch from one strategy to another without changing its own implementation.

I chose this pattern because it fits naturally with a finance application and shows how behavior can be changed dynamically.

---

## Project Structure

```text
starter/
│
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
└── README.md
```

---

## Running the Application

From the project root, run:

```bash
python main.py
```

The application processes several transactions, updates the balance, notifies the observers, adapts an external freelance income, and demonstrates the budgeting strategies.

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

## Reflection

This project helped me understand design patterns much better because I had to use them in a real application instead of only reading their definitions.

At first, some of the patterns felt like they added extra classes for a small project. After implementing them, I could see why they are useful. For example, the Adapter kept the external transaction format away from the main transaction logic, and the Observer made it possible to add balance notifications without modifying the `Balance` class every time.

The Strategy pattern was also interesting because I could change the budgeting method without changing the rest of the application.

One trade-off is that the project now contains more files and classes than a very simple finance script would need. However, I think the structure is clearer and would be easier to extend if the application became larger.

If I continued this project, I would add persistent storage, more validation, additional budget strategies, and possibly an undo feature using the Command pattern.