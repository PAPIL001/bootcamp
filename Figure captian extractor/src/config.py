# src/config.py
class Settings:
    def __init__(self):
        self.sqlite_path = "paper_data.sqlite"  # Matches your DataStorage default

def get_settings():
    return Settings()