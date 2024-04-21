"""
This file defines enumeration classes for representing task types and statuses
within a Kanban system.

- `Tasktype`: An enum class representing the different types of tasks (e.g., Epic, Task, Subtask).
- `Taskstatus`: An enum class representing the different statuses of tasks (e.g., Draft, Open, Active, Complete, Discarded).
"""
import enum


class Tasktype(enum.Enum):
    """
    An enum class representing the different types of tasks in the Kanban system.
    """
    epic = "Epic"
    """
    A high-level goal or objective that can be broken down into smaller tasks.
    """
    task = "Task"
    """
    A standalone unit of work that can be completed independently.
    """
    subtask = "Subtask"
    """
    A smaller unit of work that is part of an Epic.
    """


class Taskstatus(enum.Enum):
    """
    An enum class representing the different statuses of tasks in the Kanban system.
    """
    draft = "Draft"
    """
    A task that is still being created or edited.
    """
    open = "Open"
    """
    A task that is ready to be worked on.
    """
    active = "Active"
    """
    A task that is currently being worked on.
    """
    complete = "Complete"
    """
    A task that has been finished.
    """
    discarded = "Discarded"
    """
    A task that has been abandoned or deemed unnecessary.
    """
