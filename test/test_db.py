"""
TODO figure out db mocking...

# Import necessary libraries
from unittest.mock import patch, Mock, call
import pytest
#from pymongo.errors import ConnectionError
from pymongo import MongoClient

from module import enums
# Import functions and classes from your original file
from module.db import Wrapper, deserializeMultiple  # Replace with actual filename
from module.persistence import item


# Define a fixture to mock pymongo.MongoClient
@pytest.fixture
def mock_client():
    return Mock(MongoClient)


# Define a fixture to mock the connection object
@pytest.fixture
def mock_connection(mock_client):
    mock_client.return_value.get_database.return_value.get_collection.return_value = Mock()
    return mock_client.return_value.get_database.return_value.get_collection.return_value


def test_wrapper_init(mock_client):
    # Test successful initialization
    wrapper = Wrapper()
    assert wrapper.uri == "mongodb://localhost:27017"
    assert wrapper.dbContext == "kanban"
    assert wrapper.collection == "showcase"
    mock_client.assert_called_once_with(
        "mongodb://localhost:27017",
        connect=True,
        maxPoolSize=5,
        minPoolSize=0,
        appname="KanbanGUI.py",
        connectTimeoutMS=5000
    )


def test_wrapper_init_connection_error(mock_client):
    # Test initialization with ConnectionError
    mock_client.side_effect = ConnectionError("Failed to connect to MongoDB")
    with pytest.raises(ConnectionError):
        Wrapper()


def test_read_all(mock_connection):
    # Mock the find method to return a list
    mock_connection.find.return_value = [{"key": "item1"}, {"key": "item2"}]
    wrapper = Wrapper()
    result = wrapper.readAll()
    assert len(result) == 2
    assert deserializeMultiple.called  # Assert deserializeMultiple is called


def test_read_status(mock_connection):
    # Mock the find method to return a list with specific status
    mock_connection.find.return_value = [{"key": "item1", "status": "TODO"}]
    wrapper = Wrapper()
    result = wrapper.readStatus(enums.Taskstatus.TODO)
    assert len(result) == 1
    assert deserializeMultiple.called  # Assert deserializeMultiple is called


def test_update_item_success(mock_connection):
    # Mock methods to simulate successful update
    mock_connection.count_documents.return_value = 1
    mock_connection.update_one.return_value = Mock()
    wrapper = Wrapper()
    assert wrapper.updateItem(Mock(key="item1"))


def test_update_item_failure_not_found(mock_connection):
    # Mock count_documents to return 0 (not found)
    mock_connection.count_documents.return_value = 0
    wrapper = Wrapper()
    assert not wrapper.updateItem(Mock(key="item1"))


def test_insert_item_success(mock_connection):
    # Mock count_documents to return 0 (not found) and insert_one
    mock_connection.count_documents.return_value = 0
    mock_connection.insert_one.return_value = Mock()
    wrapper = Wrapper()
    item = Mock(key="item1")
    assert wrapper.insertItem(item)


def test_insert_item_failure_exists(mock_connection):
    # Mock count_documents to return 1 (exists)
    mock_connection.count_documents.return_value = 1
    wrapper = Wrapper()
    item = Mock(key="item1")
    assert not wrapper.insertItem(item)


def test_key_exists_success(mock_connection):
    # Mock count_documents to return 1 (exists)
    mock_connection.count_documents.return_value = 1
    wrapper = Wrapper()
    assert wrapper.keyExists("key1")


def test_key_exists_failure(mock_connection):
    # Mock count_documents to return 0 (not found)
    mock_connection.count_documents.return_value = 0
    wrapper = Wrapper()
    assert not wrapper.keyExists("key1")


def test_deserialize_multiple(mock_deserialize):
    # Mock deserialize function and assert it's called for each document
    documents = [{"key": "item1"}, {"key": "item2"}]
    mock_deserialize.side_effect = [Mock(item), Mock(item)]  # Mock item objects
    result = deserializeMultiple(documents)
    assert len(result) == 2
    mock_deserialize.assert_has_calls([call(doc) for doc in documents])

"""