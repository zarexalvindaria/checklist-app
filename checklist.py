# Checklist GUI application
import tkinter as tk

# Define window
root = tk.Tk()
root.title("Checklist")
root.iconbitmap("check.ico")
root.geometry("400x400")
root.resizable(0,0)

# Define fonts and colors
my_font = ("Times New Roman", 12)
root_color = "#6c1cbc"
button_color = "#e2cff4"
root.config(bg=root_color)

# Define functions



# Define layout
# Create frames
input_frame = tk.Frame(root, bg=root_color)
output_frame = tk.Frame(root, bg=root_color)
button_frame = tk.Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

# Input frame layout
list_entry = tk.Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = tk.Button(input_frame, text="Add Item", borderwidth=2, font=my_font, bg=button_color)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

# Output frame layout
my_scrollbar = tk.Scrollbar(output_frame)
my_listbox = tk.Listbox(output_frame, height=15, width=45, borderwidth=3, font=my_font)
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

# Button Frame layout
list_remove_button = tk.Button(button_frame, text="Remove Item", borderwidth=2, font=my_font, bg=button_color)
list_clear_button = tk.Button(button_frame, text="Clear List", borderwidth=2, font=my_font, bg=button_color)
save_button = tk.Button(button_frame, text="Save List", borderwidth=2, font=my_font, bg=button_color)
quit_button = tk.Button(button_frame, text="Quit", borderwidth=2, font=my_font, bg=button_color, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)

# Run the root window
root.mainloop()
