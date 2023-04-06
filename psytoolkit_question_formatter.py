'''
A simple formatter for making questionaires in PsyToolbox faster by Jakub Jędrusiak.
'''

import sys
import os
import tkinter
import customtkinter as CTk
from PIL import Image, ImageTk


CTk.set_appearance_mode("dark")  # Modes: system (default), light, dark

type_group_free = ["radio", "drop"] # o: free
type_group_requied = ["check"] # o: requied

def format_text():
    '''
    Main formatting function
    '''
    text = input_text.get("1.0", "end").strip()
    label_text = label_input.get().strip()
    lines = text.split("\n")
    scale = scale_text.get("1.0", "end").strip()
    answers = scale.split("\n")
    q_type = question_type.get()
    output = ""
    count = 1  # for labels
    for line in lines:
        output += f"l: {label_text}_{count}\nt: {q_type}\n"
        if random.get():
            output += "o: random\n"
        if link.get():
            output += "o: link\n"
        if q_type in type_group_free and free.get():
            output += "o: free\n"
        if q_type in type_group_requied and requied.get():
            output += "o: requied"
            if min_entry.get() != "":
                output += f" {min_entry.get().strip()}"
                if max_entry.get() != "":
                    output += f" {max_entry.get().strip()}"
        output += "\n"
        if sep.get():
            output += "o: sep\n"
        if qf.get():
            output += "o: qf\n"
        if button_input.get().strip() != "":
            output += f"b: {button_input.get().strip()}\n"
        output += f"q: {line}\n"
        for scale_entry in answers:
            output += f"- {scale_entry}\n"
        output += "\n"
        count += 1
    output_text.delete("1.0", "end")
    output_text.insert("1.0", output.strip())


def copy_to_clipboard():
    '''
    Copy to clipboard function
    '''
    formatted_text = output_text.get("1.0", "end").strip()
    if formatted_text:
        root.clipboard_clear()
        root.clipboard_append(formatted_text)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# root
root = CTk.CTk()
root.title("PsyToolkit Questionnaire Formatter")
photo = ImageTk.PhotoImage(file=resource_path("./images/brain.png"))
root.wm_iconphoto(True, photo)
left_frame = CTk.CTkFrame(root)
left_frame.grid(row=2, column=0, padx=10, pady=10)
right_frame = CTk.CTkFrame(root)
right_frame.grid(row=2, column=1, padx=10, pady=10, sticky="n")

# Options checkboxes
random = tkinter.BooleanVar()
link = tkinter.BooleanVar()
free = tkinter.BooleanVar()
requied = tkinter.BooleanVar()
sep = tkinter.BooleanVar()
qf = tkinter.BooleanVar()

random_button = CTk.CTkCheckBox(
    right_frame, text="Show items in a random order", variable=random)
link_button = CTk.CTkCheckBox(
    right_frame, text="Link to previous question (typically not necessary)", variable=link)
free_button = CTk.CTkCheckBox(
    right_frame, text="Do not require participant to select any item", variable=free)
requied_button = CTk.CTkCheckBox(
    right_frame, text="Require participant to select any item", variable=requied)
sep_button = CTk.CTkCheckBox(
    right_frame, text="Save data anonymously", variable=sep)
qf_button = CTk.CTkCheckBox(
    right_frame, text="Show question text above image/video (if any)", variable=qf)

options_buttons = ["random_button", "link_button",
                   "free_button", "requied_button", "sep_button", "qf_button"]


def clean_options():
    '''
    clears options checkboxes
    '''
    for widget in options_buttons:
        globals()[widget].pack_forget()


def show_options(question_type_selected):
    '''
    shows options checkboxes based on question type
    '''
    clean_options()
    for widget in options_buttons:
        globals()[widget].pack(pady=5, anchor="w")
    if question_type_selected in type_group_free:
        requied_button.pack_forget()
    elif question_type_selected in type_group_requied:
        free_button.pack_forget()
        requied_button.configure(command=requied_borders)

min_label = CTk.CTkLabel(right_frame, text="Minimum requied:")
min_entry = CTk.CTkEntry(right_frame, width=300)
max_label = CTk.CTkLabel(right_frame, text="Maximum requied:")
max_entry = CTk.CTkEntry(right_frame, width=300)

def requied_borders():
    '''
    minimum and maximum textboxes for o: requied
    '''
    if question_type.get() in type_group_requied and requied.get():
        min_label.pack()
        min_entry.pack()
        max_label.pack()
        max_entry.pack()
    else:
        min_label.pack_forget()
        min_entry.pack_forget()
        max_label.pack_forget()
        max_entry.pack_forget()

# Dropdown menu for selecting type of input
question_type = CTk.StringVar(value="radio")
input_label = CTk.CTkLabel(root, text="Question type:")
input_label.grid(row=0, column=0, pady=(5, 0), padx=10, sticky='w')
input_menu = CTk.CTkOptionMenu(
    root, values=type_group_free+type_group_requied, variable=question_type, command=show_options)
input_menu.grid(row=1, column=0, padx=10, columnspan=2, sticky='ew')

# Left frame
input_label = CTk.CTkLabel(left_frame, text="Enter text:")
input_label.pack()

input_text = CTk.CTkTextbox(left_frame, height=250, width=600)
input_text.pack()

label_label = CTk.CTkLabel(left_frame, text="Enter label:")
label_label.pack()

label_input = CTk.CTkEntry(left_frame, width=300)
label_input.pack()

format_button = CTk.CTkButton(left_frame, text="Format", command=format_text)
format_button.pack(pady=10)

output_label = CTk.CTkLabel(left_frame, text="Formatted text:")
output_label.pack()

output_text = CTk.CTkTextbox(left_frame, height=250, width=600)
output_text.pack()

copy_button = CTk.CTkButton(
    left_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side="bottom", pady=5)

# Scale
scale_label = CTk.CTkLabel(right_frame, text="Enter scale values:")
scale_label.pack()

scale_text = CTk.CTkTextbox(right_frame)
scale_text.pack()

button_label = CTk.CTkLabel(
    right_frame, text="Non-standard continue button text:")
button_label.pack()

button_input = CTk.CTkEntry(right_frame, width=300)
button_input.pack()

show_options(question_type.get())

root.resizable(False, False)

root.mainloop()
