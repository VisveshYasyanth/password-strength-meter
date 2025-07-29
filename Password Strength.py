import customtkinter as ctk
import re

# Appearance settings
ctk.set_appearance_mode("dark")  # Light, Dark, or System
ctk.set_default_color_theme("green")  # blue, green, dark-blue

# Create main app window
app = ctk.CTk()
app.geometry("520x460")
app.title("🏰 CastleLock: Your Password Shield")

# Dynamic font scaling based on screen width
screen_width = app.winfo_screenwidth()

# Scale factor for fonts
if screen_width >= 2560:  # 4K or ultrawide
    scale = 1.5
elif screen_width >= 1920:  # 1080p
    scale = 1.2
else:  # 720p or smaller
    scale = 1.0

# Stylish fonts
title_font = ctk.CTkFont(family="Gabriola", size=int(30 * scale), weight="bold")
label_font = ctk.CTkFont(family="Segoe UI Semibold", size=int(16 * scale))
result_font = ctk.CTkFont(family="Verdana", size=int(18 * scale), weight="bold")
detail_font = ctk.CTkFont(family="Fira Code", size=int(14 * scale))

# Check password strength logic
def check_strength():
    password = entry.get()

    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password) is not None
    lower = re.search(r"[a-z]", password) is not None
    digit = re.search(r"\d", password) is not None
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length, upper, lower, digit, special])

    # Strength level and color
    if score == 5:
        strength = "💎 Very Strong"
        color = "spring green"
    elif score == 4:
        strength = "✅ Strong"
        color = "deepskyblue"
    elif score == 3:
        strength = "⚠ Moderate"
        color = "gold"
    elif score == 2:
        strength = "❌ Weak"
        color = "tomato"
    else:
        strength = "🚫 Very Weak"
        color = "red"

    # Update result
    result_label.configure(text=f"Strength: {strength}", text_color=color)

    details = (
        f"• At least 8 characters : {'✔' if length else '❌'}\n"
        f"• Uppercase letter      : {'✔' if upper else '❌'}\n"
        f"• Lowercase letter      : {'✔' if lower else '❌'}\n"
        f"• Number                : {'✔' if digit else '❌'}\n"
        f"• Special character     : {'✔' if special else '❌'}"
    )
    detail_label.configure(text=details)

# GUI Layout
title = ctk.CTkLabel(app, text="🏰 CastleLock: Your Password Shield", font=title_font, text_color="#E6E6FA")
title.pack(pady=20)

entry = ctk.CTkEntry(app, width=350, font=label_font, placeholder_text="Enter your password", corner_radius=8)
entry.pack(pady=15)

check_btn = ctk.CTkButton(app, text="Check Password Strength", command=check_strength, font=label_font)
check_btn.pack(pady=15)

result_label = ctk.CTkLabel(app, text="", font=result_font)
result_label.pack(pady=10)

detail_label = ctk.CTkLabel(app, text="", font=detail_font, justify="left")
detail_label.pack(pady=10)

# Run app
app.mainloop()


