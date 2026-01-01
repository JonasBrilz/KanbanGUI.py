"""
This file defines functions for creating various buttons used in the Kanban board application's GUI.

It utilizes the ttkbootstrap library for creating visually appealing buttons with custom styles. Each function
provides clear documentation on its purpose, parameters, and return values.

The buttons created include:

- `listButton`: Creates a button to display a list of all Kanban board items.
- `fileButton`: Creates a button to open a file located within the project root directory.
- `websiteButton`: Creates a button to open a specified URL in the user's default web browser.
- `creationButton`: Creates a button to initiate the process of creating a new Kanban board item.
- `refreshButton`: Creates a button to refresh the entire Kanban board display.

Additionally, helper functions `openFromProjectRoot` and `openURL` are defined to handle file opening and URL launching,
respectively. These functions raise `FileNotFoundError` if the specified file is not found.
"""

import os
import webbrowser

import ttkbootstrap as tb

from . import itemGUI


def listButton(root: tb.Frame, container: tb.Frame, r: int, c: int) -> tb.Button:
    """
    Creates a button to list all items.

    :param root: The ttkbootstrap root window.
    :param container: the ttkbootstrap root widget.
    :param r: The row number for the button.
    :param c: The column number for the button.

    :return: ttkbootstrap.Button to list all items.
    """
    button = tb.Button(
        root,
        text="List All",
        command=lambda: itemGUI.listItems(container),
        style="KanbanGUI.TButton",
    )
    button.grid(row=r, column=c, ipady=15, ipadx=15, pady=5, padx=5)
    return button


def fileButton(
    root: tb.Frame, r: int, c: int, labelText: str, fileName: str
) -> tb.Button:
    """
    Creates a button to open a file from the project root.

    :param root: The tkinter root window.
    :param r: The row number for the button.
    :param c: The column number for the button.
    :param labelText: The text to display on the button.
    :param fileName: The relative path to the file from the project root.

    :return: ttkbootstrap.Button to open file under given path from project root.
    """
    Button = tb.Button(
        root,
        text=labelText,
        command=lambda: openFromResources(fileName),
        style="KanbanGUI.TButton",
    )
    Button.grid(row=r, column=c, ipady=15, ipadx=15, pady=5, padx=5)
    return Button


def websiteButton(
    root: tb.Frame, r: int, c: int, labelText: str, url: str
) -> tb.Button:
    """
    Creates a button to open a URL in default browser.

    :param root: The tkinter root window.
    :param r: The row number for the button.
    :param c: The column number for the button.
    :param labelText: The text to display on the button.
    :param url: The URL to open.

    :return: ttkbootstrap.Button to open given URL in default browser.
    """
    Button = tb.Button(
        root, text=labelText, command=lambda: openURL(url), style="KanbanGUI.TButton"
    )
    Button.grid(row=r, column=c, ipady=15, ipadx=15, pady=5, padx=5)
    return Button


def creationButton(root: tb.Frame, container: tb.Frame, r: int, c: int) -> tb.Button:
    """
    Creates a button to create a new item.

    :param root: The tkinter root window.
    :param container: The buttons parent container.
    :param r: The row number for the button.
    :param c: The column number for the button.

    :return: ttkbootstrap.Button to create a new item.
    """
    Button = tb.Button(
        root,
        text="Add Item",
        command=lambda: itemGUI.createItem(container),
        style="KanbanGUI.TButton",
    )
    Button.grid(row=r, column=c, ipady=15, ipadx=15, pady=5, padx=5)
    return Button


def openFromResources(fileName: str) -> None:
    """
    Opens a file from the project root in the default browser.

    :param fileName: The relative path to the file from the project root.

    :raises FileNotFoundError: If the file is not found.
    """
    path = os.path.dirname(__file__) + "/../" + fileName

    if os.path.isfile(path):  # Check if the file exists
        webbrowser.open_new(path)  # Open in browser
    else:
        # raise FileNotFoundError(f"File not found: {path}")
        raise FileNotFoundError(f"File not found: {fileName}")


def openURL(url: str) -> None:
    """
    Opens given URL in default Browser

    :param url: The relative path to the file from the project root.
    :type url: str
    """
    webbrowser.open_new(url)  # Open in browser


def refreshButton(root: tb.Window, r: int, c: int) -> tb.Button:
    """
    Creates a button that refreshes all columns.

    :param root: The parent widget
    :param r: The row number for the first button.
    :param c: The column number for the buttons.

    :return: The refresh button.
    """
    tb.Style().configure(foreground="#00f000", style="refresh.TButton", font=("", 20))
    Button = tb.Button(
        root,
        text="Refresh",
        command=lambda: itemGUI.refresh(root),
        style="refresh.TButton",
    )
    Button.grid(row=r, column=c, ipady=15, ipadx=15, pady=5, padx=5)
    return Button
