import inspect
import os
import tkinter as tk
import ttkbootstrap as tb

from unittest import mock
import pytest

from module import boardUtil


# Define a pytest fixture to provide a mock Tkinter root window
@pytest.fixture
def mock_root():
    return mock.Mock(spec=tk.Tk())  # Replace tkinter with your actual import


def test_openFromResources_success():
    # Create a temporary file within the test directory (assuming pytest)
    test_file = "resources/test_file.txt"
    test_path = os.path.dirname(__file__) + '/../'

    # Write some content to the test file
    with open(test_path + test_file, 'w+') as f:
        f.write("Test content")

    # Call the function to open the file (assuming boardUtil.openFromResources is defined elsewhere)
    boardUtil.openFromResources(test_file)

    # Assert the file was created (more complex checks can be added later)
    assert os.path.isfile(test_path + test_file)
    os.remove(test_path+ test_file)



def test_openFromResources_failure():
    # Define a non-existent file path
    test_file = "resources/test_file.txt"
    test_path = os.path.dirname(__file__) + '/../'

    # Call the function and assert FileNotFoundError is raised
    with pytest.raises(FileNotFoundError) as excinfo:
        boardUtil.openFromResources(test_file)

    assert str(excinfo.value) == f"File not found: {test_file}"


def test_openURL(mock_root):
    # Define a test URL
    test_url = "https://www.google.com"

    # Mock the webbrowser.open_new function
    with mock.patch("webbrowser.open_new") as mock_open:
        boardUtil.openURL(test_url)
        # Assert the mock function was called with the correct URL
        mock_open.assert_called_once_with(test_url)



"""
TODO unmute tests
def test_listButton(mock_root):
    # Simulate the container frame
    container = tk.Frame(mock_root)

    # Call the function and assert button text
    button = boardUtil.listButton(mock_root, container, 1, 1)
    assert button.config("text")[0] == "List All"


def test_fileButton_success(mock_root, tmpdir):
    # Create a temporary file
    test_file = tmpdir.join("test_file.txt")
    test_file.write("Test content")

    # Call the function and assert no exception raised
    boardUtil.fileButton(mock_root, 1, 1, "Open File", str(test_file))
    # Assert the file was opened (more complex checks can be added)
    assert os.path.isfile(test_file)


def test_fileButton_failure(mock_root):
    # Define a non-existent file path
    filename = "non_existent_file.txt"

    # Call the function and assert FileNotFoundError is raised
    with pytest.raises(FileNotFoundError) as excinfo:
        boardUtil.fileButton(mock_root, 1, 1, "Open File", filename)
    assert str(excinfo.value) == f"File not found: {os.path.abspath(filename)}"


def test_websiteButton(mock_root):
    # Define a test URL
    test_url = "https://www.google.com"

    # Mock the webbrowser.open_new function
    with mock.patch("webbrowser.open_new") as mock_open:
        boardUtil.websiteButton(mock_root, 1, 1, "Open Website", test_url)
        # Assert the mock function was called with the correct URL
        mock_open.assert_called_once_with(test_url)
"""
"""
TODO unmute tests
def test_openFromResources_success(tmpdir):
    # Create a temporary file
    #test_file = tmpdir.join("test_file.txt")
    #test_file.write("Test content")

    test_file = os.path.dirname(__file__) + '/../' + "resources/test_file.txt"
    test_file.write("Test content")

    # Call the function and assert no exception raised
    boardUtil.openFromResources(str(test_file))
    # Assert the file was opened (more complex checks can be added)
    assert os.path.isfile(test_file)
    """

""" 
TODO unmute test
def test_refreshButton(mock_root):
    # Simulate calling itemGUI.refresh (complex mocking might be needed)
    mock_root.refresh = mock.Mock()

    # Call the function and assert the mock function is called
    Button = boardUtil.refreshButton(mock_root, 1, 1)
    Button.pack()
    assert isinstance(Button, tb.Widget)
    #mock_root.refresh.assert_called_once()
"""