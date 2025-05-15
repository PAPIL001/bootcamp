import pickle
from typing import Tuple


class Game:
    def __init__(self, player_name: str, level: int = 1, score: int = 0, position: Tuple[int, int] = (0, 0)):
        self.player_name = player_name
        self.level = level
        self.score = score
        self.position = position  # (x, y) coordinates

    def move(self, dx: int, dy: int):
        x,y = self.position
        self.position = (x+dx, y+dy)

    def level_up(self):
        self.level += 1

    def increase_score(self, points: int):
        self.score += points

    def save_state(self, filename: str):
        with open(filename, "wb") as f:
            pickle.dump(self,f)

    @classmethod
    def load_state(cls, filename: str) -> "Game":
        with open(filename, "rb") as f:
            return pickle.load(f)

    def __repr__(self):
        return f"Game(player_name={self.player_name}, level={self.level}, score={self.score}, position={self.position})"

game = Game("Geetha")
game.move(5,3)
game.level_up()
game.increase_score(100)

print("Before saving:")
print(game)

# save game state
game.save_state("game_save.pkl")

# load game state
restored_game = Game.load_state("game_save.pkl")

print("\nAfter restoring:")
print(restored_game)