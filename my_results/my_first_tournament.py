import axelrod as axl
import matplotlib.pyplot as plt
from axelrod.strategies.titfortat import ZDTitForTat
from axelrod.strategies.adaptive import ZDAdaptive


def my_first_tournament(conv_round, extra_round):
    players = [s() for s in axl.axelrod_first_strategies] + [ZDTitForTat(conv_round, extra_round), ZDAdaptive(conv_round, extra_round)]
    players.append(axl.Random())
    tournament = axl.Tournament(players, turns=200, repetitions=5, seed=7 )
    results = tournament.play()
    plot = axl.Plot(results)
    plot.boxplot()
    plt.xlabel("Strategies")
    plt.ylabel("Scores")
    plt.savefig(f"my_first_axelrod_rankings_{conv_round}_{extra_round}_7.png")

# varying number of convergence rounds
my_first_tournament(30, 20)
my_first_tournament(50, 20)
my_first_tournament(100, 20)
my_first_tournament(150, 20)

# varying number of extra rounds
# my_first_tournament(50, 10)
# my_first_tournament(50, 30)
# my_first_tournament(50, 50)

# varying number of extra rounds for most performant convergence round
my_first_tournament(150, 5)
my_first_tournament(150, 10)
my_first_tournament(150, 30)
my_first_tournament(150, 40)
