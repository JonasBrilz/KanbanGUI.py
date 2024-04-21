"""
This file implements the main graphical user interface (GUI) for the Kanban board application.

It creates the main window, sets up its layout, defines custom styles, and creates the necessary widgets for navigation,
interaction, and displaying Kanban board items.

The GUI design utilizes the ttkbootstrap library for a modern and visually appealing appearance.

- 'startup': starts up the kanban graphical user interface using preconfigured parameters.
"""
import ttkbootstrap as tb

import boardUtil
from module.itemGUI import icon


def startup() -> None:
    """
    Initializes and sets up the main graphical user interface (GUI) for the Kanban board application.
    """
    # Create the main window
    root = tb.Window(themename="superhero")
    root.title("KanbanGUI.py")
    root.iconbitmap(icon())

    # Set the minimum size of the window
    root.minsize(800, 600)

    # Center the window
    root.position_center()

    # Maximize the window
    root.state('zoomed')

    # Create custom styles for increased font size
    tb.Style().configure("KanbanGUI.TButton", font=("", 20))
    tb.Style().configure("KanbanGUI.TLabel", font=("", 20))

    # Create a reference Frame at the top of the window
    refFrame = tb.Frame(root)
    refFrame.grid(row=0, column=0)

    # Create a container Frame for items
    container = tb.Frame(root)
    container.grid(row=3, column=0)

    # Create refresh, website, file, list, and creation buttons to the reference Frame
    boardUtil.refreshButton(refFrame, 0, 0)
    boardUtil.websiteButton(refFrame, 0, 1, "GitHub", "https://github.com/JonasBrilz/KanbanGUI.py")
    boardUtil.fileButton(refFrame, 0, 2, "Documentation", "resources/documentation_german.pdf")
    boardUtil.listButton(refFrame, container, 0, 3)
    boardUtil.creationButton(refFrame, container, 0, 4)

    # Create labels for the different stages of the kanban board
    tb.Label(refFrame, style="KanbanGUI.TLabel", text="Draft").grid(row=2, column=0)  # draftLabel
    tb.Label(refFrame, style="KanbanGUI.TLabel", text="Open").grid(row=2, column=1)  # openLabel
    tb.Label(refFrame, style="KanbanGUI.TLabel", text="Active").grid(row=2, column=2)  # activeLabel
    tb.Label(refFrame, style="KanbanGUI.TLabel", text="Complete").grid(row=2, column=3)  # completeLabel
    tb.Label(refFrame, style="KanbanGUI.TLabel", text="Discarded").grid(row=2, column=4)  # discardedLabel

    # Start the main event loop for the window to handle user interactions
    root.mainloop()


if __name__ == '__main__':
    startup()
