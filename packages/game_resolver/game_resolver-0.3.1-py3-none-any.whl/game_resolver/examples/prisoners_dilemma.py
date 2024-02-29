import numpy as np

from game_resolver.game import Game
from game_resolver.player import Player


# ゲームの内容をクラスとして定義する。Type3のケース。
class PrisonersDilemma(Game):
    def __init__(self) -> None:
        super().__init__()

        # 行動のインスタンス化（ndarrayで定義）
        actions = np.array(["C", "D"])

        # Payoff Matrix を直接定義。行と列に注意すること！
        payoff_matrix1 = np.array([[3, 0], [5, 1]])
        payoff_matrix2 = np.array([[3, 5], [0, 1]])

        # プレイヤのインスタンス化
        player1 = Player(0, actions=actions, payoff_matrix=payoff_matrix1)
        player2 = Player(1, actions=actions, payoff_matrix=payoff_matrix2)
        self.add(player1)
        self.add(player2)
