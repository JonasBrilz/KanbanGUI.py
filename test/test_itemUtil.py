import pytest
from unittest.mock import patch, Mock

import ttkbootstrap as tb

from module.itemUtil import (
    tasktypes,
    taskstates,
    entryPair,
    labelPair,
    entryText,
    comboPair,
    datePair,
)
from module.enums import Tasktype, Taskstatus

# Mock ttk.Frame for testing widget interactions
@pytest.fixture
def mock_root():
    mock_frame = Mock(spec=tb.Frame)
    mock_frame.grid = Mock()
    return mock_frame

def test_tasktypes():
    """
    TODO: rework this test
    """
    # Simulate Tasktype enum with some values
    expected = [member.value for member in Tasktype]

    assert tasktypes() == expected


def test_taskstates():
    """
        TODO: rework this test
    """
    # Simulate Taskstatus enum with some values
    expected = [member.value for member in Taskstatus]

    assert taskstates() == expected

"""
TODO: figure out ttkbootstrap/tkinter testing and rework tests
def test_entryPair(mock_root):
    label_text = "Name"
    fill_text = "John Doe"

    entry = entryPair(mock_root, 0, label_text, fill_text)

    assert entry.get() == fill_text
    mock_root.grid.assert_called_once_with(
        row=0, column=0, padx=(10, 0), pady=(10, 0)
    )


def test_labelPair(mock_root):
    label_text = "Status"
    fill_text = "Open"

    label = labelPair(mock_root, 1, label_text, fill_text)

    assert label.cget("text") == fill_text
    mock_root.grid.assert_any_call(row=1, column=0, padx=(10, 0), pady=(10, 0))
    mock_root.grid.assert_any_call(row=1, column=1, padx=(10, 0), pady=(10, 0))


def test_entryText(mock_root):
    label_text = "Description"
    fill_text = "This is a long description."

    text_area = entryText(mock_root, 2, label_text, fill_text)

    assert text_area.get("1.0", "end-1c") == fill_text
    mock_root.grid.assert_any_call(row=2, column=0, padx=(10, 0), pady=(10, 0))
    mock_root.grid.assert_any_call(row=2, column=1, padx=(10, 0), pady=(10, 0))


def test_comboPair(mock_root):
    label_text = "Priority"
    options = ["High", "Medium", "Low"]
    preset_value = "Medium"

    combo = comboPair(mock_root, 3, label_text, options, preset_value)

    assert combo.current() == options.index(preset_value)
    mock_root.grid.assert_any_call(row=3, column=0, padx=(10, 0), pady=(10, 0))
    mock_root.grid.assert_any_call(row=3, column=1, padx=(10, 0), pady=(10, 0))


def test_datePair(mock_root):
    label_text = "Due Date"

    date_entry = datePair(mock_root, 4, label_text)

    assert isinstance(date_entry, tb.DateEntry)
    mock_root.grid.assert_any_call(row=4, column=0, padx=(10, 0), pady=(10, 0))
    mock_root.grid.assert_any_call(row=4, column=1, padx=(10, 0), pady=(10, 0))
    
"""
