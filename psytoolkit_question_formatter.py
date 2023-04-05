'''
A simple formatter for making questionaires in PsyToolbox faster by Jakub Jędrusiak.
'''

import tkinter
import customtkinter as CTk

CTk.set_appearance_mode("dark")  # Modes: system (default), light, dark


def format_text():
    '''
    Main formatting function
    '''
    text = input_text.get("1.0", "end").strip()
    label_text = label_input.get().strip()
    lines = text.split("\n")
    scale = scale_text.get("1.0", "end").strip()
    answers = scale.split("\n")
    output = ""
    count = 1 # for labels
    for line in lines:
        output += f"l: {label_text}_{count}\nt: radio\n"
        if random.get():
            output += "o: random\n"
        if link.get():
            output += "o: link\n"
        if free.get():
            output += "o: free\n"
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

root = CTk.CTk()
root.title("PsyToolkit Questionnaire Formatter")

# Left frame for text input, label, and format button
left_frame = CTk.CTkFrame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10)

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

# Right frame for scale entries and options
right_frame = CTk.CTkFrame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Checkbox for random answer order
random = tkinter.BooleanVar()
random_button = CTk.CTkCheckBox(
    right_frame, text="Show items in a random order", variable=random)
random_button.pack(pady=5, anchor="w")

link = tkinter.BooleanVar()
link_button = CTk.CTkCheckBox(
    right_frame, text="Link to previous question (typically not necessary)", variable=link)
link_button.pack(pady=5, anchor="w")

free = tkinter.BooleanVar()
free_button = CTk.CTkCheckBox(
    right_frame, text="Do not require participant to select any item", variable=free)
free_button.pack(pady=5, anchor="w")

sep = tkinter.BooleanVar()
sep_button = CTk.CTkCheckBox(
    right_frame, text="Save data anonymously", variable=sep)
sep_button.pack(pady=5, anchor="w")

qf = tkinter.BooleanVar()
qf_button = CTk.CTkCheckBox(
    right_frame, text="Show question text above image/video (if any)", variable=qf)
qf_button.pack(pady=5, anchor="w")

scale_label = CTk.CTkLabel(right_frame, text="Enter scale values:")
scale_label.pack()

scale_text = CTk.CTkTextbox(right_frame)
scale_text.pack()

button_label = CTk.CTkLabel(right_frame, text="Non-standard continue button text:")
button_label.pack()

button_input = CTk.CTkEntry(right_frame, width=300)
button_input.pack()

root.resizable(False, False)

root.mainloop()
