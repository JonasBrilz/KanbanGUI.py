"""
This file provides utility functions for creating consistent label-widget pairs
within a Ttkbootstrap grid layout. It also includes functions for retrieving task type
and status options for use in comboboxes and other selections.

- 'tasktypes': Returns a list of task types as strings.
- 'taskstates': Returns a list of task states as strings.
- 'entryPair': Creates a label-entry pair for single-line text input.
- 'labelPair': Creates a label-label pair for displaying information.
- 'entryText': Creates a label-text area pair for multi-line text input.
- 'comboPair': Creates a label-combobox pair for selecting from options.
- 'datePair': Creates a label-date entry pair for selecting a date.
"""
import ttkbootstrap as tb

import module.enums


def tasktypes() -> list[str]:
    """
    Returns a list of task type options.

    This function iterates through the members of the enums.Tasktype enum class
    and extracts their string values. These values represent the different task types
    available in the system.

    :return: A list containing all task type options as strings.
    """
    return [member.value for member in module.enums.Tasktype]


def taskstates() -> list[str]:
    """
    Returns a list of task state options.

    This function iterates through the members of the enums.Taskstatus enum class
    and extracts their string values. These values represent the different task states
    available in the system (e.g., draft, in progress, completed).

    :return: A list containing all task state options as strings.
    """
    return [member.value for member in module.enums.Taskstatus]


def entryPair(root: tb.Frame, r: int, labelText: str, fillText: str = "") -> tb.Entry:
    """
    Creates a label-entry pair for user input.

    This function creates a label with the provided text and an entry widget.
    The entry widget is initially filled with the optional `fillText` parameter.
    The label and entry are then placed in a grid layout within the `root` widget.

    :param root: The parent widget where the label-entry pair will be placed.
    :param r: The row index for placing the label-entry pair in the grid.
    :param labelText: The text to be displayed on the label.
    :param fillText: The initial text to be filled in the entry widget. Defaults to "".

    :return: The created entry widget.
    """
    label = tb.Label(root, text=labelText + ": ")
    entry = tb.Entry(root)
    entry.insert(0, fillText)

    label.grid(row=r, column=0, padx=(10, 0), pady=(10, 0))
    entry.grid(row=r, column=1, padx=(10, 0), pady=(10, 0))
    return entry


def labelPair(root: tb.Frame, r: int, labelText: str, fillText: str) -> tb.Label:
    """
    Creates a label-label pair for displaying information.

    This function creates a label with the provided `labelText` and another label
    with the provided `fillText`. Both labels are then placed in a grid layout
    within the `root` widget.

    :param root: The parent widget where the label-label pair will be placed.
    :param r: The row index for placing the label-label pair in the grid.
    :param labelText: The text to be displayed on the first label.
    :param fillText: The text to be displayed on the second label.

    :return: The created label widget.
    """

    label = tb.Label(root, text=labelText + ": ")
    readOnly = tb.Label(root, text=fillText)

    label.grid(row=r, column=0, padx=(10, 0), pady=(10, 0))
    readOnly.grid(row=r, column=1, padx=(10, 0), pady=(10, 0))
    return readOnly


def entryText(root, r, labelText, fillText="") -> tb.Text:
    """
    Creates a label-text area pair for multi-line user input.

    This function creates a label with the provided `labelText` and a text area widget.
    The text area is initially filled with the optional `fillText` parameter.
    The label and text area are then placed in a grid layout within the `root` widget.

    :param root: The parent widget where the label-text area pair will be placed.
    :param r: The row index for placing the label-text area pair in the grid.
    :param labelText: The text to be displayed on the label.
    :param fillText: The initial text to be filled in the text area. Defaults to "".

    :return: The created text area widget.
    """
    label = tb.Label(root, text=labelText + ": ")
    textEntry = tb.Text(root, height=10, width=30)
    textEntry.insert("1.0", fillText)

    label.grid(row=r, column=0, padx=(10, 0), pady=(10, 0))
    textEntry.grid(row=r, column=1, padx=(10, 0), pady=(10, 0))
    return textEntry


def comboPair(root, r, labelText, options, preset_value=None) -> tb.Combobox:
    """
    Creates a label-combobox pair for selecting from predefined options.

    This function creates a label with the provided `labelText` and a combobox widget.
    The combobox is populated with the provided `options` list. If a `preset_value`
    is provided, it will be pre-selected in the combobox. The label and combobox
    are then placed in a grid layout within the `root` widget.

    :param root: The parent widget where the label-combobox pair will be placed.
    :param r: The row index for placing the label-combobox pair in the grid.
    :param labelText): The text to be displayed on the label.
    :param options: A list of options to be displayed in the combobox.
    :param preset_value: The value to be pre-selected in the combobox. Defaults to None.

    :return: The created combobox widget.
    """
    label = tb.Label(root, text=labelText + ": ")
    combo = tb.Combobox(root, values=options, state='readonly')
    if preset_value:
        combo.current(options.index(preset_value))

    label.grid(row=r, column=0, padx=(10, 0), pady=(10, 0))
    combo.grid(row=r, column=1, padx=(10, 0), pady=(10, 0))
    return combo


def datePair(root, r, labelText) -> tb.DateEntry:
    """
    Creates a label-date entry pair for selecting a date.

    This function creates a label with the provided `labelText` and a date entry widget.
    The label and date entry are then placed in a grid layout within the `root` widget.

    :param root: The parent widget where the label-date entry pair will be placed.
    :param r: The row index for placing the label-date entry pair in the grid.
    :param labelText: The text to be displayed on the label.

    :return: The created date entry widget.
    """
    label = tb.Label(root, text=labelText + ": ")
    date = tb.DateEntry(root)

    label.grid(row=r, column=0, padx=(10, 0), pady=(10, 0))
    date.grid(row=r, column=1, padx=(10, 0), pady=(10, 0))
    return date
