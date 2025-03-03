import axelrod as axl
import matplotlib.pyplot as plt
from axelrod.strategies.titfortat import ZDTitForTat
from axelrod.strategies.adaptive import ZDAdaptive


def my_plotkin_tournament(conv_round, extra_round):
    players = [
        axl.Cooperator(),
        axl.Defector(),
        axl.ZDExtort2(),
        axl.HardGoByMajority(),
        axl.FirstByJoss(),
        axl.HardTitForTat(),
        axl.HardTitFor2Tats(),
        axl.TitForTat(),
        axl.Grudger(),
        axl.GTFT(),
        axl.TitFor2Tats(),
        axl.WinShiftLoseStay(),
        axl.Random(),
        axl.ZDGTFT2()
        ] 
    players = players + [ZDTitForTat(conv_round, extra_round), ZDAdaptive(conv_round, extra_round)]
    tournament = axl.Tournament(
        players=players,
        turns=200,
        repetitions=5,
        seed=7
        )
    results = tournament.play()
    plot = axl.Plot(results)
    plot.boxplot()
    plt.xlabel("Strategies")
    plt.ylabel("Scores")
    plt.savefig(f"my_plotkin_rankings_{conv_round}_{extra_round}_7.png")

# varying number of convergence rounds
my_plotkin_tournament(30, 20)
my_plotkin_tournament(50, 20)
my_plotkin_tournament(100, 20)
my_plotkin_tournament(150, 20)

# varying number of extra rounds
my_plotkin_tournament(150, 5)
my_plotkin_tournament(150, 10)
my_plotkin_tournament(150, 30)
my_plotkin_tournament(150, 40)
