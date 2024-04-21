"""
This package contains functionality for testing this projects functional scripts.

Modules:
- test.boardUtil: Contains utility functions for creating UI elements with predefined functionality
- test.db: Contains the 'Wrapper'-class, which provides functionality to control data interchange
        between this application and a database
        also contains functions to deserialize multiple items (defined in module.persistence)
        and read credentials from the resources/credentials.txt file.
- test.itemGUI: Contains functions for creating UI elements to interact with information stored in the database
- test.itemUtil: Contains utility functions for creating UI elements with consistent styling
        within a ttkbootstrap grid layout.
- test.persistence: Provides classes and functions for persisting Kanban tasks
        to and from a MongoDB database.

no tests for:
- module.__main__: Contains 'startup', combining tkinter and ttkbootstrap widgets with this projects functionality.
        All operations are imported from other packages.
- module.enums: Script defines two enums, no testable functionality present.

This package leverages the following external libraries:

- pymongo: For interacting with a MongoDB database.
- tkinter: For creating visually appealing UI elements.
- ttkbootstrap: For creating visually appealing UI elements.

- pytest: Ergonomics for setting up tests and execution.
- unittest: Ergonomics for setting up tests.
"""
