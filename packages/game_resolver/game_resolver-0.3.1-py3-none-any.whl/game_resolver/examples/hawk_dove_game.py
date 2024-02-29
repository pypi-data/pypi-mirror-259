import numpy as np

from game_resolver.game import Game
from game_resolver.payoff import Payoff
from game_resolver.player import Player


# ゲームの内容をクラスとして定義する。Type4のケース。
class HawkDoveGame(Game):
    def __init__(self) -> None:
        super().__init__()

        # 行動のインスタンス化（ndarrayで定義）
        actions = np.array(["Hawk", "Dove"])

        # Payoff のインスタンス化
        payoff1 = Payoff()
        payoff1.set(("Hawk", "Hawk"), -2)
        payoff1.set(("Hawk", "Dove"), 4)
        payoff1.set(("Dove", "Hawk"), 0)
        payoff1.set(("Dove", "Dove"), 2)

        payoff2 = Payoff()
        payoff2.set(("Hawk", "Hawk"), -2)
        payoff2.set(("Hawk", "Dove"), 0)
        payoff2.set(("Dove", "Hawk"), 4)
        payoff2.set(("Dove", "Dove"), 2)

        # プレイヤのインスタンス化
        player1 = Player(0, actions=actions, payoff=payoff1)
        player2 = Player(1, actions=actions, payoff=payoff2)
        self.add(player1)
        self.add(player2)
