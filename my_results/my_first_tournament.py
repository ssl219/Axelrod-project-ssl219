import axelrod as axl
import matplotlib.pyplot as plt
from axelrod.strategies.titfortat import ZDTitForTat


def my_first_tournament(conv_round, extra_round):
    players = [s() for s in axl.axelrod_first_strategies] + [ZDTitForTat(conv_round, extra_round)]
    players.append(axl.Random())
    tournament = axl.Tournament(players)
    results = tournament.play()
    plot = axl.Plot(results)
    plot.boxplot()
    plt.savefig(f"my_first_axelrod_rankings_{conv_round}_{extra_round}.png")
    # p.show()

# varying number of convergence rounds
my_first_tournament(30, 20)
my_first_tournament(50, 20)
my_first_tournament(100, 20)
my_first_tournament(150, 20)

# varying number of extra rounds
# my_first_tournament(50, 10)
# my_first_tournament(50, 30)
# my_first_tournament(50, 50)
# my_first_tournament(150, 5)
# my_first_tournament(150, 10)
# my_first_tournament(150, 30)
# my_first_tournament(150, 40)
