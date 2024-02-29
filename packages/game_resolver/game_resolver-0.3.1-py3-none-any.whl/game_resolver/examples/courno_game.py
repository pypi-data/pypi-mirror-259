# ゲームの内容をクラスとして定義する。Type1のケース。
import numpy as np

from game_resolver.game import Game
from game_resolver.player import Player


class CournotGame(Game):
    def __init__(self) -> None:
        super().__init__()

        # 行動のインスタンス化（ndarrayで定義）
        actions = np.arange(1, 100, 0.1)

        # プレイヤのインスタンス化
        player1 = Player(0, actions=actions, payoff_function=self.payoff_function1)
        player2 = Player(1, actions=actions, payoff_function=self.payoff_function2)
        self.add(player1)
        self.add(player2)

    # 利得関数を定義
    def payoff_function1(self, action1: float, action2: float) -> float:
        return (100 - action1 - action2) * action1 - 40 * action1

    def payoff_function2(self, action1: float, action2: float) -> float:
        return (100 - action1 - action2) * action2 - 40 * action2
