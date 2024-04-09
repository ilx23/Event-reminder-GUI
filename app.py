# Import required module
from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Initial height of the application window.
app_height = 310


def add_event():
    """
    Function to add an event to the GUI.
    It retrieves event details from user input, validates them,
    and displays the event along with a reminder if it's in the future.
    """
    global app_height
    name = event_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    # Check if any field is empty.
    if name == "" or date == "" or time == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        try:
            # Convert date and time strings to datetime object.
            event_datetime = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
            current_datetime = datetime.now()

            # Check if the event time is in the future.
            if event_datetime < current_datetime:
                messagebox.showerror("Error", "Please enter a future time for your event")
            else:
                # Clear input fields.
                event_entry.delete(0, END)
                date_entry.delete(0, END)
                time_entry.delete(0, END)

                # Display event name and date on the GUI.
                event_label = Label(event_frame, text=name, font=("aria", 12))
                event_label.pack()

                event_date_label = Label(event_frame, text=f"{event_datetime}", font=("aria", 10), fg="grey")
                event_date_label.pack(pady=5)

                # Adjust application window height dynamically.
                app_height += 60
                app.geometry(f"400x{app_height}")

                # Calculate time difference for the reminder.
                delta = event_datetime - current_datetime
                seconds = delta.total_seconds()
                reminder_in_ms = seconds * 1000

                # Set a reminder to show a message box at the event time.
                app.after(int(reminder_in_ms),
                          lambda: messagebox.showinfo("Reminder", f"Don't forget your event: {name}"))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date and time")


def clear_event():
    """
    Function to clear all events from the GUI and reset the application window size.
    """
    global app_height
    for widget in event_frame.winfo_children():
        widget.destroy()
    app.geometry("400x310")
    event_frame.config(height=1)
    app_height = 310


# Create the Tkinter application window.
app = Tk()
app.title("Event Reminder On GUI")
app.geometry("400x310")
app.config(padx=10, pady=10)

# GUI components: Labels, Entry fields, Buttons.
app_title = Label(app, text="Event Reminder", font=("Nectar Bold", 20))
app_title.pack()

event_name = Label(app, text="Enter Event Name", font=("aria", 12))
event_name.pack(pady=5)

event_entry = Entry(app, font="aria", borderwidth=2, relief=GROOVE)
event_entry.pack()

date_label = Label(app, text="Date (YYYY-MM-DD)", font=("aria", 12))
date_label.pack()

date_entry = Entry(app, font="aria", borderwidth=2, relief=GROOVE)
date_entry.pack()

time_label = Label(app, text="Time (HH:MM)", font=('aria', 12))
time_label.pack()

time_entry = Entry(app, font="aria", borderwidth=2, relief=GROOVE)
time_entry.pack()

set_button = Button(app, text="Set Event", font=("aria", 12), borderwidth=2, relief=GROOVE, command=add_event)
set_button.pack(pady=10)

event_frame = Frame(app)
event_frame.pack()

clear_button = Button(app, text="Clear", font="aria", borderwidth=2, relief=GROOVE, command=clear_event)
clear_button.pack(pady=5)

# Start the Tkinter event loop.
app.mainloop()

time_label = Label(app, text="Time (HH:MM)", font=('aria', 12))
time_label.pack()

time_entry = Entry(app, font="aria", borderwidth=2, relief=GROOVE)
time_entry.pack()

set_button = Button(app, text="Set Event", font=("aria", 12), borderwidth=2, relief=GROOVE, command=add_event)
set_button.pack(pady=10)

event_frame = Frame(app)
event_frame.pack()

clear_button = Button(app, text="Clear", font="aria", borderwidth=2, relief=GROOVE, command=clear_event)
clear_button.pack(pady=5)

app.mainloop()
