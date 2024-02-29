from typing import List

from game_resolver.player import Player


class Game:
    def __init__(self) -> None:
        self.player_list: List[Player] = []

    def add(self, player: Player) -> None:
        self.player_list.append(player)
