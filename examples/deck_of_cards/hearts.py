import sys


class HeartsGame:
    def __init__(self, *names: str) -> None:
        self.names = (list(names) + "P1 P2 P3 P4".split())[:4]


if __name__ == "__main__":
    player_names = sys.argv[1:]
    game = HeartsGame(*player_names)
    game.play()
