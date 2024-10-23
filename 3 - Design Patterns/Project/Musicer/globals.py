class GlobalSettings:
    def __init__(self):
        self.volume = 50
        self.theme = "light"

    def adjust_volume(self, volume):
        self.volume = volume
        print(f"User volume set to {self.volume}")

    def set_theme(self, theme):
        self.theme = theme
        print(f"User theme set to {self.theme}")