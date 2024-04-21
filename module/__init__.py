"""
This package provides functionality for managing Kanban tasks within a Python application.

Modules:
- module.__main__: Contains 'startup', a function for starting up the application and the primary kanban-board interface.
- module.boardUtil: Contains utility functions for creating UI elements with predefined functionality
- module.db: Contains the 'Wrapper'-class, which provides functionality to control data interchange
        between this application and a database
        also contains functions to deserialize multiple items (defined in module.persistence)
        and read credentials from the resources/credentials.txt file.
- module.enums: Defines enumeration classes for task types and statuses.
- module.itemGUI: Contains functions for creating UI elements to interact with information stored in the database
- module.itemUtil: Contains utility functions for creating UI elements with consistent styling
        within a ttkbootstrap grid layout.
- module.persistence: Provides classes and functions for persisting Kanban tasks
        to and from a MongoDB database.

This package leverages the following external libraries:

- pymongo: For interacting with a MongoDB database.
- tkinter: For creating visually appealing UI elements.
- ttkbootstrap: For creating visually appealing UI elements.
"""
