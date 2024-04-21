''' TODO unmute tests
import pytest

from module import persistence, enums


@pytest.mark.parametrize(
    "item1, item2, expected_equal",
    [
        # equal attributes
        (
                persistence.item("KEY1", enums.Tasktype.task, "1 January 2024", 3, 1,
                                 enums.Taskstatus.active, "Fix bug", None, []),
                persistence.item("KEY1", enums.Tasktype.task, "1 January 2024", 3, 1,
                                 enums.Taskstatus.active, "Fix bug", None, []),
                True,
        ),
        # different attributes
        (
                persistence.item("Marketing Q1", enums.Tasktype.epic, "2024-01-01 18:00:00", "3H", "1H",
                                 enums.Taskstatus.discarded, "Fix bug", None, []),
                persistence.item("Marketing Q1", enums.Tasktype.epic, "2024-01-01 18:00:00", "3H", "1H",
                                 enums.Taskstatus.complete, "Fix bug", None, []),
                False,
        ),
        (
                persistence.item("Marketing Q1", enums.Tasktype.epic, "2024-01-01 18:00:00", "3H",
                                 "1H", enums.Taskstatus.discarded, "Fix bug", None, []),
                persistence.item("Marketing Q2", enums.Tasktype.task, "2025-01-01 18:00:00", "60H",
                                 "10H", enums.Taskstatus.complete, "Fix multiple bugs",
                                 "SampleTask1", [{"timestamp": "2025-01-01 19:32:11", "comment": "SampleComment"}]),
                False,
        ),
        # single different type
        (
                persistence.item("Marketing Q1", enums.Tasktype.epic, "2024-01-01 18:00:00", "3H",
                                 "1H", enums.Taskstatus.discarded, "Fix bug", None, []),
                "Not an item",
                False
        ),
        # two different types
        (
                {"key": "KEY1"},
                "Not an item",
                False
        ),
    ],
)
def test_item_equality(item1, item2, expected_equal):
    assert (item1 == item2) == expected_equal


@pytest.mark.parametrize(
    "valid_data", [
        (
                {
                    "key": "123",
                    "type": "Task",
                    "creation": "2024-03-13T00:00:00",
                    "estimate": 4,
                    "time_spent": 2,
                    "status": "Progress",
                    "description": "This is a test task",
                    "parent": None,
                    "history": []
                }
        ),
        (
                {
                    "key": "Marketing Q1",
                    "type": "Subtask",
                    "creation": "2024-05-13T00:00:00",
                    "estimate": "8760 Hours",
                    "time_spent": "3600 seconds",
                    "status": "Progress",
                    "description": "This is a test Marketing-Task",
                    "parent": "Marketing-Parent-Task",
                    "history":
                        [
                            {"timestamp": "yesterday",
                             "comment": "another sample comment"
                             }
                        ]
                }
        ),
    ]
)
def test_deserialize_valid_data(valid_data):
    """
    Tests that deserialize works correctly with valid input data.
    """
    expected_item = persistence.item(valid_data["key"],
                                     valid_data["type"],
                                     valid_data["creation"],
                                     valid_data["estimate"],
                                     valid_data["time_spent"],
                                     valid_data["status"],
                                     valid_data["description"],
                                     valid_data["parent"],
                                     valid_data["history"])

    # Call the function under test
    deserialized_item = persistence.deserialize(valid_data)

    # Assert that the returned item is equal to the expected item
    assert deserialized_item == expected_item


@pytest.mark.parametrize(
    "invalid_data",
    [
        {
            "type": "Task",
            "creation": "2024-03-13T00:00:00",
            "estimate": 4,
            "time_spent": 2,
            "status": "Progress",
            "description": "This is a test task",
            "parent": None,
            "history": []
        },
        {
            "type": "Task",
            "creation": "2024-03-13T00:00:00",
            "estimate": "4 Hours",
            "time_spent": "2 Hours",
            "status": "Progress",
            "description": "This is a test task",
            "parent": None,
            "history": []
        },
        {
            "type": "Task",
            "creation": "2024-03-13T00:00:00",
            "estimate": "4 Hours",
            "time_spent": "2 Hours",
            "status": "Progress",
            "description": "LeBron James",
            "parent": None,
            "history": []
        }
    ]
)
def test_deserialize_missing_key(invalid_data):
    """
    Tests that deserialize raises an appropriate exception
    when a required key is missing from the input data.
    """

    # Expected exception type
    expected_exception = KeyError

    with pytest.raises(expected_exception) as excinfo:
        persistence.deserialize(invalid_data)



@pytest.mark.parametrize(
    "item, expected",
    [
        persistence.item("123", enums.Tasktype.task, "2024-03-13T00:00:00", 4, 2,
                         enums.Taskstatus.active, "This is a test task", None, []),
        {
            "key": "123",
            "type": "Task",
            "creation": "2024-03-13T00:00:00",
            "estimate": 4,
            "time_spent": 2,
            "status": "Active",
            "description": "This is a test task",
            "parent": None,
            "history": []
        }
    ]
)
def test_insert_dict(item, expected):
    assert item.insertDict().__eq__(expected)
'''

'''
TODO unmute tests
@pytest.mark.parametrize(
    "item, expected",
    [
        persistence.item(
            "123",
            enums.Tasktype.task,
            "2024-03-13T00:00:00",
            4,
            2,
            enums.Taskstatus.active,
            "This is a test task",
            None,
            []
        ),
        {
            "type": "Task",
            "time_spent": 2,
            "status": "Active",
            "description": "This is a test task",
            "parent": None,
            "history": []
        }
    ]
)
def test_update_dict(item, expected):
    assert item.updateDict() == expected
'''