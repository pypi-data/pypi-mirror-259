from typing import Callable, Optional, cast

import numpy as np

from game_resolver.payoff import Payoff


class Player:
    def __init__(
        self,
        id: int,
        actions: np.ndarray,
        payoff: Optional[Payoff] = None,
        payoff_function: Optional[Callable] = None,
        payoff_matrix: Optional[np.ndarray] = None,
    ) -> None:
        self.id = id
        self.actions = actions
        self.payoff: Payoff = cast(Payoff, payoff)
        self.payoff_function: Callable = cast(Callable, payoff_function)
        self.payoff_matrix: np.ndarray = cast(np.ndarray, payoff_matrix)
