import itertools
import math
from typing import Dict, List, Tuple

import numpy as np
from tqdm import tqdm

from game_resolver.game import Game


class NashEquilibrium:
    def __init__(self, game: Game) -> None:
        self.game = game

        # 各プレイヤが持つ行動の選択肢のリスト
        self.actions_list = [p.actions for p in game.player_list]

        # payoff matrix の次元
        self.dim = tuple([len(i) for i in self.actions_list])

        # 利得関数の定義の仕方によるタイプ分け処理
        self.check_payoff_definition_type()

    def check_payoff_definition_type(self) -> None:
        """
        利得関数の定義の仕方によるタイプ分けを行う
        - Type1: 全てbroadcastを使う。高速に処理可能。
        - Type2: Payoff Matrix の生成に for文を使う。Type1より遅い。
        - Type3: 直接 Payoff Matrixを定義するため初期化処理が必要ない。小規模なゲーム向き。
        - Type4: Payoffクラスのインスタンス化を使う。Type2よりさらに遅い。
        """

        # ↓優先順が最も低い
        if self.game.player_list[0].payoff is not None:
            self.type = 4
        # ↓2番目に優先順が高い（両方設定されていたら上書きする）
        if self.game.player_list[0].payoff_function is not None:
            # 各プレイヤの戦略を2つだけ取り出して、payoff_functionでbroadcastできるかチェック
            actions_for_check = [
                np.array([p.actions[0], p.actions[1]]) for p in self.game.player_list
            ]
            try:
                self.game.player_list[0].payoff_function(*actions_for_check)
                # エラーが出なければ、以下が続けて実行される
                self.type = 1
            except ValueError:  # エラーをキャッチして処理を進める
                self.type = 2
        # ↓最も優先順が高い（両方設定されていたら上書きする）
        if self.game.player_list[0].payoff_matrix is not None:
            self.type = 3

        # 直接定義されていない場合 (Type1, 2, 4)
        if self.type in [1, 2, 4]:
            # まず次元数dimを使って、全プレイヤ分のpayoff matrixを0で初期化
            for player in self.game.player_list:
                player.payoff_matrix = np.zeros(self.dim).copy()

        # Type 毎に初期化が異なる。ただし、type3は初期化無しでOK。
        if self.type == 1:
            self.initialize_payoff_matrices()
        elif self.type == 2:
            self.initialize_payoff_matrices_without_broadcasting()
        elif self.type == 3:
            pass
        elif self.type == 4:
            self.initialize_payoff_matrices_from_payoff_instance()
        else:
            raise ValueError("利得が正しく設定できていません。")

    # type hint は後で
    def initialize_payoff_matrices_from_payoff_instance(self) -> None:
        # 各プレイヤが持つ行動の選択肢のindexのリスト
        actlins_idx_list = [
            [i for i in range(len(p.actions))] for p in self.game.player_list
        ]

        # 全プレイヤ分の payoff matrixを作成
        total_repetition = math.prod([len(i) for i in self.actions_list])
        bar = tqdm(total=total_repetition)
        for profile, idx in zip(
            itertools.product(*self.actions_list), itertools.product(*actlins_idx_list)
        ):
            for player in self.game.player_list:
                player.payoff_matrix[idx] = player.payoff.get(profile)

            bar.update()

    # type hint は後で
    def initialize_payoff_matrices_without_broadcasting(self) -> None:
        # 各プレイヤが持つ行動の選択肢のリスト
        actions_list = [p.actions for p in self.game.player_list]
        # 各プレイヤが持つ行動の選択肢のindexのリスト
        actlins_idx_list = [
            [i for i in range(len(p.actions))] for p in self.game.player_list
        ]

        # 全プレイヤ分の payoff matrixを作成
        total_repetition = math.prod([len(i) for i in actions_list])
        bar = tqdm(total=total_repetition)
        for profile, idx in zip(
            itertools.product(*actions_list), itertools.product(*actlins_idx_list)
        ):
            for player in self.game.player_list:
                player.payoff_matrix[idx] = player.payoff_function(*list(profile))
            bar.update()

    # これが基本の初期化（broadcastを使う。最も高速。）
    def initialize_payoff_matrices(self) -> None:
        # 各プレイヤが持つ行動の選択肢のリスト
        actions_list = []

        for idx, player in tqdm(enumerate(self.game.player_list)):
            # dim は [1,1,1,1,len(player.actions),1,1] のような形式
            # index のところだけ自分の戦略集合の要素数になるようにする
            dim = [
                1 if i != idx else len(player.actions)
                for i in range(len(self.game.player_list))
            ]

            # この reshape はナッシュ均衡計算で broadcast するため
            actions_list.append(player.actions.reshape(dim))

        for player in tqdm(self.game.player_list):
            # for文を使わず Broadcast で一発でMatrixをセット
            player.payoff_matrix = player.payoff_function(*actions_list)

    def get_nash_equilibrium(self) -> Dict:
        # まずはTrueのMatrixを作成 (Broadcastするのでサイズは1で初期化)
        nash_bool_matrix: np.ndarray = np.ones((1), dtype=bool)

        for idx, player in tqdm(enumerate(self.game.player_list)):
            # axis=idx にすることで、そのプレイヤの最適反応を一発で取れる
            br_matrix = player.payoff_matrix.max(axis=idx, keepdims=True)

            # Matrixのうちで最適反応になっている要素だけTrueにする
            br_bool_matrix = player.payoff_matrix >= br_matrix

            # for文で全てのplayerについて、順にbool値を掛け算していく
            # Matrixの中で最後までTrueであれば、その要素（セル）がNash
            nash_bool_matrix = nash_bool_matrix * br_bool_matrix

        # 出力のための整形
        _nash_indices = np.where(nash_bool_matrix == [True])
        nash_indices: List[Tuple] = []  # 整形後のindex(タプル)のリスト
        nash_profile_list = []
        nash_payoff_list = []
        for idx in zip(*_nash_indices):
            nash_indices.append(idx)
            profile = [p.actions[i] for i, p in zip(idx, self.game.player_list)]
            nash_profile_list.append(profile)
            nash_payoff_list.append(
                [p.payoff_matrix[idx] for p in self.game.player_list]
            )

        result_dict = {
            "index": nash_indices,
            "profile": nash_profile_list,
            "payoff": nash_payoff_list,
        }

        return result_dict
