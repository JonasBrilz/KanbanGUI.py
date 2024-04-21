"""
This file defines the `item` class to represent tasks within the Kanban application.

- `item`: A class representing a task with attributes like key, type, creation date,
         estimated time, time spent, status, description, parent task, and history of changes.
- `deserialize`: A function that deserializes a dictionary representation of a Task object
                 back into a Task object.
"""
from module.enums import Tasktype, Taskstatus


class item:
    """
    This class represents a task within the application.

    A task has various attributes including a unique identifier, type, creation date,
    estimated time, time spent, current status, description, optional parent task,
    and a history of changes.
    """
    def __init__(self, key, type: Tasktype, creation, estimate, time_spent, status: Taskstatus, description, parent,
                 history) -> None:
        """
        This method initializes a new Task object.

        :param key: The unique identifier for the task.
        :param type: The type of task (e.g., Epic, Task, Subtask).
        :param creation: The date and time the task was created.
        :param estimate: The estimated time required to complete the task.
        :param time_spent: The amount of time spent working on the task so far.
        :param status: The current status of the task .
        :param description: A textual description of the task.
        :param parent: The optional identifier of the parent task (if applicable).
        :param history: A list containing historical changes to the task attributes.
        """
        self.key = key
        self.type: Tasktype = type
        self.creation = creation
        self.estimate = estimate
        self.time_spent = time_spent
        self.status: Taskstatus = status
        self.description = description
        self.parent = parent
        self.history = history

    def __eq__(self, other) -> bool:
        """
        This method defines equality comparison for the Task class.

        :param other: Another Task object to compare with.

        :return: True if all attributes of the tasks are equal, False otherwise.
        """
        if not isinstance(other, item):
            return False

        return (
                self.key == other.key and
                self.type == other.type and
                self.creation == other.creation and
                self.estimate == other.estimate and
                self.time_spent == other.time_spent and
                self.status == other.status and
                self.description == other.description and
                self.parent == other.parent and
                self.history == other.history
        )

    def insertDict(self) -> dict[str, str]:
        """
        This method creates a dictionary representation of the Task object
        suitable for insertion into a database or other storage mechanism.

        :return: A dictionary containing all attributes of the Task object as strings.
        """
        return {
            "key": f"{self.key}",
            "type": f"{self.type}",
            "creation": f"{self.creation}",
            "estimate": f"{self.estimate}",
            "time_spent": f"{self.time_spent}",
            "status": f"{self.status}",
            "description": f"{self.description}",
            "parent": f"{self.parent}",
            "history": self.history
        }

    def updateDict(self) -> dict:
        """
        This method creates a dictionary representation of the Task object
        suitable for updating existing data in a database or other storage mechanism.

        :return: A dictionary containing only attributes that can be modified after creation.
        """
        return {
            "type": f"{self.type}",
            "time_spent": f"{self.time_spent}",
            "status": f"{self.status}",
            "description": f"{self.description}",
            "parent": f"{self.parent}",
            "history": self.history
        }


def deserialize(doc: dict) -> item:
    """
    This function deserializes a dictionary representation of a Task object
    back into a Task object.

    :param doc: A dictionary containing the serialized data of a Task object.

    :return: A Task object created from the provided dictionary.
    """
    return item(doc["key"],
                doc["type"],
                doc["creation"],
                doc["estimate"],
                doc["time_spent"],
                doc["status"],
                doc["description"],
                doc["parent"],
                doc["history"])
