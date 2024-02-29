import numpy as np

from game_resolver.game import Game
from game_resolver.player import Player


# ゲームの内容をクラスとして定義する。Type2のケース。
class BattleOfSex(Game):
    def __init__(self) -> None:
        super().__init__()

        # 行動のインスタンス化（ndarrayで定義）
        actions = np.array(["Boxing", "Ballet"])

        # プレイヤのインスタンス化
        player1 = Player(
            0, actions=actions, payoff_function=self.player1_payoff_function
        )
        player2 = Player(
            1, actions=actions, payoff_function=self.player2_payoff_function
        )
        self.add(player1)
        self.add(player2)

    def player1_payoff_function(self, player1_action: str, player2_action: str) -> int:
        if player1_action == "Boxing":
            if player2_action == "Boxing":
                return 2
            elif player2_action == "Ballet":
                return 0
            else:
                raise ValueError("未定義の戦略が入力されています。")
        elif player1_action == "Ballet":
            if player2_action == "Boxing":
                return 0
            elif player2_action == "Ballet":
                return 1
            else:
                raise ValueError("未定義の戦略が入力されています。")
        else:
            raise ValueError("未定義の戦略が入力されています。")

    def player2_payoff_function(self, player1_action: str, player2_action: str) -> int:
        if player1_action == "Boxing":
            if player2_action == "Boxing":
                return 1
            elif player2_action == "Ballet":
                return 0
            else:
                raise ValueError("未定義の戦略が入力されています。")
        elif player1_action == "Ballet":
            if player2_action == "Boxing":
                return 0
            elif player2_action == "Ballet":
                return 2
            else:
                raise ValueError("未定義の戦略が入力されています。")
        else:
            raise ValueError("未定義の戦略が入力されています。")
