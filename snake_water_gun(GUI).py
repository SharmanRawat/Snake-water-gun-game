import customtkinter as ctk
import random

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class SnakeWaterGunApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Snake Water Gun - Modern UI")
        self.geometry("500x500")

        self.points = 0
        self.name = ""

        self.label_title = ctk.CTkLabel(self, text="🐍💧🔫 Snake Water Gun Game", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=20)

        self.entry_name = ctk.CTkEntry(self, placeholder_text="Enter your name")
        self.entry_name.pack(pady=10)

        self.start_button = ctk.CTkButton(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.frame_game = ctk.CTkFrame(self)
        self.label_status = ctk.CTkLabel(self.frame_game, text="", font=("Arial", 14))
        self.label_choices = ctk.CTkLabel(self.frame_game, text="", font=("Arial", 12))
        self.label_result = ctk.CTkLabel(self.frame_game, text="", font=("Arial", 16, "bold"))
        self.label_points = ctk.CTkLabel(self.frame_game, text="Points: 0", font=("Arial", 12))

        self.buttons_frame = ctk.CTkFrame(self.frame_game)
        self.snake_btn = ctk.CTkButton(self.buttons_frame, text="Snake 🐍", command=lambda: self.play("snake"))
        self.water_btn = ctk.CTkButton(self.buttons_frame, text="Water 💧", command=lambda: self.play("water"))
        self.gun_btn = ctk.CTkButton(self.buttons_frame, text="Gun 🔫", command=lambda: self.play("gun"))

        self.quit_button = ctk.CTkButton(self.frame_game, text="Quit", command=self.quit, fg_color="red")

    def start_game(self):
        self.name = self.entry_name.get()
        if not self.name.strip():
            self.name = "Player"
        self.start_button.configure(state="disabled")
        self.entry_name.configure(state="disabled")

        self.label_status.configure(text=f"Welcome {self.name}! Let's play!")
        self.frame_game.pack(pady=10)

        self.label_status.pack(pady=5)
        self.label_choices.pack()
        self.label_result.pack(pady=5)
        self.label_points.pack()

        self.buttons_frame.pack(pady=10)
        self.snake_btn.grid(row=0, column=0, padx=5)
        self.water_btn.grid(row=0, column=1, padx=5)
        self.gun_btn.grid(row=0, column=2, padx=5)

        self.quit_button.pack(pady=10)

    def play(self, option):
        choices = ["snake", "water", "gun"]
        random_option = random.choice(choices)

        if option == random_option:
            result = "It's a draw!"
            self.points += 0
        elif option == "snake" and random_option == "water":
            result = "You win!"
            self.points += 1
        elif option == "snake" and random_option == "gun":
            result = "You lose!"
            self.points -= 1
        elif option == "water" and random_option == "gun":
            result = "You win!"
            self.points += 1
        elif option == "water" and random_option == "snake":
            result = "You lose!"
            self.points -= 1
        elif option == "gun" and random_option == "snake":
            result = "You win!"
            self.points += 1
        elif option == "gun" and random_option == "water":
            result = "You lose!"
            self.points -= 1
        else:
            result = "Invalid choice!"

        self.label_choices.configure(text=f"You: {option} | Computer: {random_option}")
        self.label_result.configure(text=result)
        self.label_points.configure(text=f"Points: {self.points}")

if __name__ == "__main__":
    app = SnakeWaterGunApp()
    app.mainloop()
