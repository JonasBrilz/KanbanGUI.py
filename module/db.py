"""
This file provides a wrapper class for interacting with a MongoDB database
to manage Kanban task items.

- `Wrapper`: A class that encapsulates MongoDB connection and data access logic
            for Kanban items.
- `deserializeMultiple`: A function that deserializes a list of MongoDB documents
                         into a list of Kanban item objects.
"""

from pymongo.mongo_client import MongoClient
from ttkbootstrap.dialogs import Messagebox
import os.path

from . import enums
from .persistence import item, deserialize


class Wrapper:
    def __init__(
        self, uri: str = None, dbcontext: str = None, collection: str = None
    ) -> None:
        """
        Initializes the Wrapper class with the given MongoDB URI, database context, and collection.

        :param uri: The MongoDB URI. Default is "mongodb://localhost:27017".
        :param dbcontext: The database context. Default is "kanban".
        :param collection: The collection. Default is "showcase".
        """
        if uri is None and dbcontext is None and collection is None:
            credentials = readCredentials("resources/credentials.txt")
            self.uri = credentials["uri"]
            self.dbcontext = credentials["dbcontext"]
            self.collection = credentials["collection"]
        else:
            self.uri = uri
            self.dbcontext = dbcontext
            self.collection = collection

        self.client = MongoClient(
            self.uri,
            connect=True,
            maxPoolSize=5,  # Maximum connections in the pool
            minPoolSize=0,  # Minimum connections when idle
            appname="KanbanGUI.py",
            connectTimeoutMS=5000,  # Timeout for establishing connections
        )
        db = self.client[self.dbcontext]
        self.connection = db[self.collection]

    def readAll(self) -> list[item]:
        """
        Reads all documents from the MongoDB collection.

        :return: A list of deserialized items.
        """
        result = self.connection.find()
        return deserializeMultiple(result)

    def readStatus(self, type: enums.Taskstatus) -> list[item]:
        """
        Reads all documents from the MongoDB collection with the given status.

        :param type: The task status.

        :return: A list of deserialized items with the given status.
        """
        criteria = {"status": type.value}
        result = self.connection.find(criteria)
        return deserializeMultiple(result)

    def updateItem(self, current: item) -> bool:
        """
        Updates the given item in the MongoDB collection if its key exists.

        :param current: The item to update.
        :return: True if the item was updated, False otherwise.
        """
        # check if key exists in db
        # if true update
        if self.keyExists(current.key):
            criteria = {"key": current.key}
            update = {"$set": current.updateDict()}
            self.connection.update_one(criteria, update)
            return True
        else:
            return False

    def insertItem(self, current: item) -> bool:
        """
        Inserts the given item into the MongoDB collection if its key does not exist.

        :param current: The item to insert.
        :return: True if the item was inserted, False otherwise.
        """
        # check if key exists in db
        if not self.keyExists(current.key):
            self.connection.insert_one(current.insertDict())
            Messagebox.ok("Item inserted", "Success")
            return True
        else:
            Messagebox.ok("Item not inserted", "Unsuccessful")
            return False

    def keyExists(self, key: str) -> bool:
        """
        Checks if the given key exists in the MongoDB collection.

        :param key: The key to check.
        :return: True if the key exists, False otherwise.
        """
        criteria = {"key": key}
        count = self.connection.count_documents(criteria, limit=1)
        return count > 0


def deserializeMultiple(documents: dict) -> list[item]:
    """
    Deserializes a MongoDB document into a Kanban item.

    :param documents: The MongoDB document to deserialize.
    :return: List of items.
    """
    items = []
    for doc in documents:
        items.append(deserialize(doc))
    return items


def readCredentials(filename):
    """
    Reads pymongo credentials from a text file.

    :param filename: filename The path to the file containing credentials.

    :return: A dictionary containing pymongo connection details.

    :raises FileNotFoundError: If the specified file is not found.
    """
    try:
        with open(os.path.dirname(__file__) + "/../" + filename, "r") as f:
            lines = f.readlines()
            credentials = {}
            for line in lines:
                key, value = line.strip().split("=")
                credentials[key] = value
            return credentials
    except FileNotFoundError:
        raise FileNotFoundError(f"Credentials file not found: {filename}")
