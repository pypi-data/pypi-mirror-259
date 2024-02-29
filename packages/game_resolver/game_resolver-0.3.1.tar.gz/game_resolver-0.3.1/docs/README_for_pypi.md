# game_resolver

This library is internal library for nishino-lab(The University of Tokyo)

http://www.css.t.u-tokyo.ac.jp

## Run Sample Game

This library has three type sample games(prisoner, battle of sex, cournot).

```python
from game_resolver.games.custom_game import Prisoner
from game_resolver.nash_equilibrium import NashEquilibrium

prisoner = Prisoner()
ne = NashEquilibrium()
eq = e.get_equilibrium(g)
for i in eq:
    print(i)
```

## Run your own game

A Nash equilibrium can be solved by representing the problem to be solved in the Game class.

```python
from game_resolver.games.custom_game import CustomGame
from game_resolver.nash_equilibrium import NashEquilibrium

player_num = 2
action_list = ["Cooperate", "Defect"]
all_player_action_list = [
    ("Cooperate", "Cooperate"),
    ("Cooperate", "Defect"),
    ("Defect", "Cooperate"),
    ("Defect", "Defect")
]
payoff_list = [
    [3, 0, 5, 1],
    [3, 5, 0, 1]
]

your_own_game = CustomGame("volunteer_dilenma",
                            player_num,
                            action_list,
                            all_player_action_list,
                            payoff_list)
e = NashEquilibrium()
eq = e.get_equilibrium(your_own_game)
for i in eq:
    print(i)
```
