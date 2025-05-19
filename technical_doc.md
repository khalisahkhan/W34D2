W34D2 After-Class Assignment: Software Design Patterns and Best Practices

Problem: A logger system that supports multiple output formats (console, file, database)

Design Patterns Used:
1. Strategy Patter - allows us to to define logging behaviors such as to console, file or database and make them interchangeable without changing the logger’s structure. Each of these console, file, database, is a seperate strategy and all follow the same rule using the log() method. 
2. Factory Method Pattern - this is used to choose and create the right logger (console, file, or database) based on a setting or user input. Instead of the main code deciding how to create each logger, the factory handles it. This makes the code clearner and easier to update later.

SOLID Principle:
Single Resposibility: Each logger class: console_logger, file_logger, and db_logger handles the responsibility of logging to a specific output.
Open/Closed: The system is open for new logger types but closed for modification of exisiting loggers.
Liskov Substitution: Any type of logger can be used whenever the logger_strategy interface is expected.
Interface Segregation: logger_strategy interface is only focused on logging and does not include extra methods.
Dependency Inversion: The main part of the program uses a general interface (logger_strategy), not specific loggers. This makes the code more flexible and easier to test without swapping in new loggers without changing the main code. 

Trade-offs and Alternatives Considered:
Decorator Pattern - can be used to add extra features like timestamps or message formatting
Observer Pattern - this lets multiple loggers work at the same time such as logging to both file and console
Direct Instantiation vs Factory - ability to use a seperate function or class handle object creation when changes need to be done

Future Extensibility:
The design makes it easy to add new types of logging in the future. You can create a nw logger class by following the same pattern, inherit from logger_strategy and then update logger_factory to include the new logger type. The setup is flexible and ready for future upgrades such as logging to cloud tools. 
