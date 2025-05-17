class Book:
    def __init__(self, title):
        self.title = title

class AudioMixin:
    def play_audio(self):
        return f"Playing audio for {self.title}"

class AudioBook(Book, AudioMixin):
    pass

ab = AudioBook("The Hobbit")
print(ab.play_audio())
# Output: Playing audio for The Hobbit
