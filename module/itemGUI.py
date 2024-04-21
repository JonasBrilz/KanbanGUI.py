"""
This file provides functionalities for managing Kanban board items
within the KanbanGUI.py application. It interacts with the database
using the `db.Wrapper` class and utilizes helper functions from `itemUtil`.

- `editItem`: Opens a window to edit the details of an existing Kanban item.
- `createItem`: Opens a window to create a new Kanban item.
- `listItems`: Opens a window to display a list of all Kanban items.
- `icon`: Returns the filepath of the application icon.
- `populateColumn`: Populates a column on the Kanban board with buttons for each item.
- `refresh`: Refreshes the Kanban board display by reading items with different statuses from the database.
- `bootstyleFromType`: Returns the appropriate ttkbootstrap style based on the task type.
"""
import datetime
import tkinter as tk
from os import path

from ttkbootstrap.dialogs import Messagebox

import ttkbootstrap as tb

from module import db, enums, itemUtil
from module.persistence import item


def editItem(root, current: item, button) -> None:
    """
    Opens a window to edit the details of an existing item.

    :param root: The main application window.
    :param current: The item to be edited.
    :param button: The button object that triggered the edit action.
    """
    childWindow = tb.Toplevel(root)
    childWindow.title("KanbanGUI.py - " + current.key)
    childWindow.iconbitmap(icon())
    childWindow.geometry("350x500")
    childWindow.position_center()

    keyLabel = itemUtil.labelPair(childWindow, 0, labelText="Key", fillText=current.key)
    typeLabel = itemUtil.comboPair(childWindow, 1, labelText="Type", options=itemUtil.tasktypes(),
                                   preset_value=current.type)
    creationLabel = itemUtil.labelPair(childWindow, 2, labelText="Creation", fillText=current.creation)
    estimateLabel = itemUtil.labelPair(childWindow, 3, labelText="Estimate", fillText=current.estimate)
    spentLabel = itemUtil.entryPair(childWindow, 4, labelText="Time Spent", fillText=current.time_spent)
    statusLabel = itemUtil.comboPair(childWindow, 5, labelText="Status", options=itemUtil.taskstates(),
                                     preset_value=current.status)
    parentLabel = itemUtil.entryPair(childWindow, 6, labelText="Parent", fillText=current.parent)
    descLabel = itemUtil.entryText(childWindow, 7, labelText="Description", fillText=current.description)

    def update():
        """
        Updates the current item in the database with the modified values.
        """
        var = item(current.key, typeLabel.get(), current.creation, current.estimate, spentLabel.get(),
                   statusLabel.get(), descLabel.get("1.0", "end"), parentLabel.get(), [])
        connection = db.Wrapper()
        if connection.updateItem(var):
            Messagebox.ok("Item inserted", "Success")
        else:
            Messagebox.ok("Item not inserted", "Unsuccessful")
        childWindow.destroy()
        button.destroy()
        refresh(root)

    tb.Button(childWindow, text="Cancel", command=lambda: childWindow.destroy(), style="warning-outline").grid(row=8,
                                                                                                               column=0)
    tb.Button(childWindow, text="Confirm", command=lambda: update(), style="success-outline").grid(row=8, column=1)


def createItem(root):
    """
    Opens a window to create a new item.

    :param root: The main application window.
    """
    childWindow = tb.Toplevel(root)
    childWindow.title("KanbanGUI.py - Add new Item")
    childWindow.iconbitmap(icon())
    childWindow.geometry("350x400")
    childWindow.position_center()

    keyLabel = itemUtil.entryPair(childWindow, 0, "Key")
    typeLabel = itemUtil.comboPair(childWindow, 1, "Type", itemUtil.tasktypes(), preset_value=enums.Tasktype.task.value)
    estimateLabel = itemUtil.entryPair(childWindow, 3, "Estimate")
    parentLabel = itemUtil.entryPair(childWindow, 2, "Parent")
    descLabel = itemUtil.entryText(childWindow, 4, "Description")

    def insert():
        """
        Inserts the new item into the database.
        """
        var = item(keyLabel.get(), typeLabel.get(), datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"),
                   estimateLabel.get(), 0,
                   enums.Taskstatus.draft.value, descLabel.get("1.0", "end"), parentLabel.get(), [])
        connection = db.Wrapper()
        connection.insertItem(var)

    tb.Button(childWindow, text="Cancel", command=lambda: childWindow.destroy(), style="warning-outline").grid(row=5,
                                                                                                               column=0)
    tb.Button(childWindow, text="Insert", command=lambda: insert(), style="success-outline").grid(row=5, column=1)


def listItems(root):
    """
    Opens a window to display a list of all items.

    :param root: The main application window.
    """
    childWindow = tb.Toplevel(root)
    childWindow.title("KanbanGUI.py - All Items")
    childWindow.geometry("200x350")
    childWindow.iconbitmap(icon())
    childWindow.position_center()

    # Create a list of items
    items = db.Wrapper().readAll()

    # Create the listbox widget
    listbox = tk.Listbox(childWindow, selectmode=tk.SINGLE, width=220)  # Enable single selection
    listbox.pack()

    # Add items to the listbox from the list
    for item in items:
        listbox.insert(tk.END, item.key)

    # Function to print the selected item based on row (index)
    def openItem(event):
        selected_index = listbox.curselection()[0]  # Get the index of the selected item
        selected_fruit = items[selected_index]  # Get the item at the selected index
        editItem(root, selected_fruit, [])

    listbox.bind("<<ListboxSelect>>", openItem)


def icon() -> str:
    """
    :return: filepath of icon.ico for this application
    """
    return path.join(path.dirname(__file__), "../resources/icon.ico")


def populateColumn(root: tb.Frame, items: list[item], r: int, c: int) -> None:
    """
    Populates a column with buttons for each item.

    :param root: The tkinter root window.
    :param items: The list of items to create buttons for.
    :param r: The row number for the first button.
    :param c: The column number for the buttons.
    """
    for item in items:
        Button = tb.Button(root, text=item.key, style=bootstyleFromType(item.type))
        Button.configure(command=lambda i=item, b=Button: editItem(root, i, b))
        Button.grid(row=r, column=c, ipady=15, ipadx=15, pady=2, padx=5)
        r += 1


def refresh(root: tk.Frame) -> None:
    """
    Refreshes the task list by reading tasks from the database with different statuses.

    :param root: The parent widget.
    """
    connection = db.Wrapper()

    draftItems = connection.readStatus(enums.Taskstatus.draft)
    openItems = connection.readStatus(enums.Taskstatus.open)
    progressItems = connection.readStatus(enums.Taskstatus.active)
    completeItems = connection.readStatus(enums.Taskstatus.complete)
    discardedItems = connection.readStatus(enums.Taskstatus.discarded)

    for widget in root.grid_slaves():
        if widget.grid_info()['row'] > 2:
            widget.destroy()

    populateColumn(root, draftItems, 3, 0)
    populateColumn(root, openItems, 3, 1)
    populateColumn(root, progressItems, 3, 2)
    populateColumn(root, completeItems, 3, 3)
    populateColumn(root, discardedItems, 3, 4)


def bootstyleFromType(currentType: enums.Tasktype) -> str:
    """
    Returns the appropriate Bootstyle for a task based on its type.

    :param currentType: The task type.
    :return: The Bootstyle.
    """
    return "success" if currentType == enums.Tasktype.epic.value else "info" if currentType == enums.Tasktype.task.value else "light"
