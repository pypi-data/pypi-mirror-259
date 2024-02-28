import tkinter as tk
import platform
import os

path = os.path.dirname(os.path.realpath(__file__))

class ContextMenuWidget(tk.Menu):
    """Extended widget with a context menu that includes Cut, Copy, and Paste commands."""

    def __init__(self, widget: tk.Widget, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize the ContextMenuWidget with a specified widget and configure it
        self.widget = widget
        self.config(tearoff=False)

        # Load icons for Cut, Copy, Paste, and Select All commands
        self.cut_icon = tk.PhotoImage(file=f"{path}/Assets/Images/edit-cut.png")
        self.copy_icon = tk.PhotoImage(file=f"{path}/Assets/Images/edit-copy.png")
        self.paste_icon = tk.PhotoImage(file=f"{path}/Assets/Images/edit-paste.png")
        self.select_all_icon = tk.PhotoImage(file=f"{path}/Assets/Images/edit-select-all.png")

        # Add menu commands with icons, accelerators, and associated functions
        self.add_command(label="Cut", image=self.cut_icon, compound="left", accelerator="Ctrl+X", command=self.popup_cut)
        self.add_command(label="Copy", image=self.copy_icon, compound="left", accelerator="Ctrl+C", command=self.popup_copy)
        self.add_command(label="Paste", image=self.paste_icon, compound="left", accelerator="Ctrl+V", command=self.popup_paste)
        self.add_separator()
        self.add_command(label="Select All", image=self.select_all_icon, compound="left", accelerator="Ctrl+A", command=self.select_all)

        # Map the right button event based on the platform (Mac or others)
        self.map_right_button_event()

        # Bind the right-click event and Ctrl+A event to the specified functions
        self.widget.bind("<<RightClick>>", self.show_menu)
        self.widget.bind("<Control-a>", self.select_all)
        self.widget.bind("<Control-A>", self.select_all)

    def map_right_button_event(self):
        """Map the right-click event based on the platform."""
        if platform.system() == "Darwin":
            self.event_add("<<RightClick>>", "<Button-2>")
        else:
            self.event_add("<<RightClick>>", "<Button-3>")

    def update_menu_state(self):
        """Update the state of menu entries based on the widget's content and clipboard status."""
        if isinstance(self.widget, tk.Text):
            widget_content = self.widget.get("1.0", tk.END).strip()
        else:
            try:
                widget_content = self.widget.get()
            except AttributeError as error:
                print(error)
                return False

        clipboard_content = self.widget.clipboard_get()
        content_available = bool(widget_content)
        # Enable or disable menu entries based on widget and clipboard content
        self.entryconfig("Cut", state="normal" if content_available else "disabled")
        self.entryconfig("Copy", state="normal" if content_available else "disabled")
        self.entryconfig("Paste", state="normal" if clipboard_content else "disabled")
        self.entryconfig("Select All", state="normal" if content_available else "disabled")

        return True

    def popup_cut(self):
        """Generate a '<<Cut>>' event for the widget."""
        self.widget.event_generate("<<Cut>>")

    def popup_copy(self):
        """Generate a '<<Copy>>' event for the widget."""
        self.widget.event_generate("<<Copy>>")

    def popup_paste(self):
        """Generate a '<<Paste>>' event for the widget."""
        self.widget.event_generate("<<Paste>>")

    def show_menu(self, event=None):
        """Display the context menu at the specified event location after updating its state."""
        if self.update_menu_state():
            self.tk_popup(event.x_root, event.y_root)

    def select_all(self, event=None):
        """Generate a '<<SelectAll>>' event for the widget and return 'break' to prevent default behavior."""
        self.widget.event_generate("<<SelectAll>>")
        return "break"
