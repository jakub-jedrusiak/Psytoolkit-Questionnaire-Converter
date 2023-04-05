'''
A simple formatter for making questionaires in PsyToolbox faster by Jakub Jędrusiak.
'''

import tkinter.messagebox as msg
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def format_text():
    text = input_text.get("1.0", "end").strip()
    label_text = label_input.get().strip()
    lines = text.split("\n")
    output = ""
    count = 1
    for line in lines:
        output += f"l: {label_text}_{count}\nt: radio\nq: {line}\n"
        for scale_entry in scale_entries:
            if scale_entry.get():
                output += f"- {scale_entry.get()}\n"
        output += "\n"
        count += 1
    output_text.delete("1.0", "end")
    output_text.insert("1.0", output.strip())

def copy_to_clipboard():
    formatted_text = output_text.get("1.0", "end").strip()
    if formatted_text:
        root.clipboard_clear()
        root.clipboard_append(formatted_text)
        msg.showinfo("Copy to Clipboard", "Formatted text copied to clipboard!")
    else:
        msg.showerror("Copy to Clipboard", "No formatted text to copy!")

def add_scale_entry():
    scale_entry = customtkinter.CTkEntry(scale_frame)
    scale_entry.pack(pady=5)
    scale_entries.append(scale_entry)

def remove_scale_entry():
    if len(scale_entries) > 1:
        scale_entry = scale_entries.pop()
        scale_entry.destroy()

root = customtkinter.CTk()
root.title("PsyToolkit Questionnaire Converter")

# Left frame for text input, label, and format button
left_frame = customtkinter.CTkFrame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10)

input_label = customtkinter.CTkLabel(left_frame, text="Enter text:")
input_label.pack()

input_text = customtkinter.CTkTextbox(left_frame, height=250, width = 600)
input_text.pack()

label_label = customtkinter.CTkLabel(left_frame, text="Enter label:")
label_label.pack()

label_input = customtkinter.CTkEntry(left_frame, width = 300)
label_input.pack()

format_button = customtkinter.CTkButton(left_frame, text="Format", command=format_text)
format_button.pack(pady=10)

output_label = customtkinter.CTkLabel(left_frame, text="Formatted text:")
output_label.pack()

output_text = customtkinter.CTkTextbox(left_frame, height=250, width = 600)
output_text.pack()

copy_button = customtkinter.CTkButton(left_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side="bottom", pady=5)

# Right frame for scale entries
right_frame = customtkinter.CTkFrame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

scale_label = customtkinter.CTkLabel(right_frame, text="Enter scale values:")
scale_label.pack()

scale_button_frame = customtkinter.CTkFrame(right_frame)
scale_button_frame.pack(pady=5)

add_button = customtkinter.CTkButton(scale_button_frame, text="+", command=add_scale_entry)
add_button.pack(side="left", padx=5)

remove_button = customtkinter.CTkButton(scale_button_frame, text="-", command=remove_scale_entry)
remove_button.pack(side="left", padx=5)

scale_frame = customtkinter.CTkFrame(right_frame)
scale_frame.pack()

scale_entries = []
scale_entry = customtkinter.CTkEntry(scale_frame)
scale_entry.pack(pady=5)
scale_entries.append(scale_entry)

root.mainloop()
