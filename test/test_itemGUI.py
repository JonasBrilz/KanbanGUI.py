import tkinter as tk

from module import itemGUI, enums
import pytest
from unittest import mock


@pytest.fixture
def mock_root():
    return mock.Mock(spec=tk.Tk())


@pytest.mark.parametrize(
    "type, expected",
    [
        # expected inputs
        (
                enums.Tasktype.epic.value,
                "success"
        ),
        (
                enums.Tasktype.task.value,
                "info"
        ),
        (
                enums.Tasktype.subtask.value,
                "light"
        ),
        # unexpected inputs
        (
                "str",
                "light"
        ),
        (
                5,
                "light"
        ),
        (
                None,
                "light"
        ),
        (
                True,
                "light"
        ),
        (
                False,
                "light"
        ),
        (
                0.0,
                "light"
        ),
        (
                Exception,
                "light"
        ),
        (
                ZeroDivisionError,
                "light"
        ),
        (
                "https://www.youtube.com/watch?v=-zd62MxKXp8",
                "light"
        )
    ]
)
def test_bootstyleFromType(type, expected):
    assert itemGUI.bootstyleFromType(type).__eq__(expected)


""" 
TODO figure out this testcase
def test_refresh(mock_root):
    # Simulate calling itemGUI.refresh (complex mocking might be needed)
    mock_root.refresh = mock_root

    # Call the function and assert the mock function is called
    itemGUI.refresh(mock_root)
    #mock_root.refresh.assert_called_once()
    mock_root.refresh.assert_has_calls()
    #mock_root.refresh.mock_add_spec(tk.tk())
"""
