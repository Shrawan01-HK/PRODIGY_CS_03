import tkinter as tk
import re

class PasswordStrengthAssessor:
    def __init__(self, master):
        self.master = master
        master.title("Password Strength Assessor")

        # Create input field for password
        self.password_frame = tk.Frame(master)
        self.password_label = tk.Label(self.password_frame, text="Enter a password:")
        self.password_label.pack(side=tk.LEFT)
        self.password_entry = tk.Entry(self.password_frame, show="*", width=40)
        self.password_entry.pack(side=tk.LEFT)
        self.password_frame.pack()

        # Create button to assess password strength
        self.assess_button = tk.Button(master, text="Assess Password Strength", command=self.assess_password_strength)
        self.assess_button.pack()

        # Create label to display feedback
        self.feedback_label = tk.Label(master, text="", wraplength=400)
        self.feedback_label.pack()

    def assess_password_strength(self):
        try:
            password = self.password_entry.get()
            feedback = self.assess_password(password)
            self.feedback_label.config(text=feedback)
        except Exception as e:
            self.feedback_label.config(text=f"Error: {e}")

    def assess_password(self, password):
        feedback = []
        strength = 0

        # Check password length
        if self.check_password_length(password):
            strength += 1
        else:
            feedback.append("Password is too short. It should be at least 8 characters long.")

        # Check for character types
        if self.check_character_types(password):
            strength += 1
        else:
            feedback.append("Password should contain at least one uppercase letter, one lowercase letter, one number, and one special character.")

        # Determine password strength based on criteria met
        if strength == 2:
            feedback = ["Strong password!"]
        elif strength == 1:
            feedback = ["Medium password. Consider adding more complexity."]
        else:
            feedback = ["Weak password. Please try again."]

        return "\n".join(feedback)

    def check_password_length(self, password):
        return len(password) >= 8

    def check_character_types(self, password):
        patterns = [
            (r"[A-Z]", "uppercase letter"),
            (r"[a-z]", "lowercase letter"),
            (r"\d", "number"),
            (r"[!@#$%^&*()_+=-{};:'<>,./?]", "special character")
        ]
        for pattern, _ in patterns:
            if not re.search(pattern, password):
                return False
        return True

root = tk.Tk()
my_gui = PasswordStrengthAssessor(root)
root.mainloop()
