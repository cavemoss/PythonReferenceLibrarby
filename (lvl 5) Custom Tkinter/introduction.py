import customtkinter

appearance_mode = 'dark'
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

root.geometry('500x350')

def login():
    print('Test')

def change_color():
    global appearance_mode
    if appearance_mode == 'dark':
        customtkinter.set_appearance_mode('light')
        appearance_mode = 'light'
    else:
        customtkinter.set_appearance_mode('dark')
        appearance_mode = 'dark'

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='Login System', font=('Roboto', 23))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='LogIn', command=login)
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='Change Color', command=change_color)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(padx=12, pady=10)

root.mainloop()
