import customtkinter as ctk
import ctypes

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

running = False
IDC_WAIT = 32514

def set_loading_cursor():
    ctypes.windll.user32.SetSystemCursor(ctypes.windll.user32.LoadCursorW(None, IDC_WAIT), 32512)

def restore_default_cursor():
    ctypes.windll.user32.SystemParametersInfoW(87, 0, None, 0)

def start_loading():
    global running
    if not running:
        running = True
        set_loading_cursor()
        update_status("✅ Active", "green")

def stop_loading():
    global running
    if running:
        running = False
        restore_default_cursor()
        update_status("❌ Inactive", "red")

def update_status(status_text, color):
    status_label.configure(text=f"Status: {status_text}", fg_color=color)
    app.title(f"Windows_Cursor_Busy_Indicator_Tool - {status_text}")

app = ctk.CTk()
app.title("Windows_Cursor_Busy_Indicator_Tool - Inactive")
app.resizable(False, False)

main_frame = ctk.CTkFrame(app, corner_radius=15)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

title_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
title_frame.pack(pady=(10, 5))

title_label = ctk.CTkLabel(title_frame, text="Windows_Cursor_Busy_Indicator_Tool", font=("Bahnschrift", 27))
title_label.pack(pady=10, padx=10)

status_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
status_frame.pack(pady=10)

status_label = ctk.CTkLabel(status_frame, text="Status: Inactive", fg_color="red", width=300, height=40, font=("Bahnschrift", 20), corner_radius=15)
status_label.pack()

button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
button_frame.pack(pady=20)

start_button = ctk.CTkButton(button_frame, text="✅ Start Loading", command=start_loading, font=("Bahnschrift", 20), fg_color="green", width=150, height=40, corner_radius=15, hover_color="#00a600")
start_button.pack(side="left", padx=10)

stop_button = ctk.CTkButton(button_frame, text="❌ Stop Loading", command=stop_loading, font=("Bahnschrift", 20), fg_color="red", width=150, height=40, corner_radius=15, hover_color="#b20000")
stop_button.pack(side="left", padx=10)

info_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
info_frame.pack(pady=10)

info_label = ctk.CTkLabel(info_frame, text="Keyboard Shortcut to stop: Ctrl+Q\nUse this shortcut to immediately stop the loading process.",
                          wraplength=400, font=("Arial", 14), justify="center")
info_label.pack()

credits_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
credits_frame.pack(side="bottom", pady=10)

credits_label = ctk.CTkLabel(credits_frame, text="Developed by: LoSh", font=("Arial", 13, "italic"))
credits_label.pack()

def on_closing(event=None):
    stop_loading()
    app.quit()

app.bind("<Control-q>", on_closing)
app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
