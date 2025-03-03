import axelrod as axl
import matplotlib.pyplot as plt
from axelrod.strategies.titfortat import ZDTitForTat
from axelrod.strategies.adaptive import ZDAdaptive
from axelrod.strategies.memoryone import WangLinInvincible


def my_ZD_tournament(conv_round, extra_round):
    players = [
        axl.ZDExtortion(),
        axl.ZDExtort2(),
        axl.ZDExtort2v2(),
        axl.ZDExtort3(),
        axl.ZDExtort4(),
        axl.ZDGen2(),
        axl.ZDGTFT2(),
        axl.ZDMischief(),
        axl.ZDSet2(), 
        axl.TitForTat()
    ]
    my_player = ZDTitForTat(conv_round, extra_round)
    players = players + [my_player, ZDAdaptive(conv_round, extra_round), WangLinInvincible()]
    players.append(axl.Random())
    tournament = axl.Tournament(players, turns=200, repetitions=5)
    results = tournament.play()
    plot = axl.Plot(results)
    plot.boxplot()
    plt.ylabel('Scores')
    plt.xlabel("Strategies")
    plt.savefig(f"my_ZD_rankings_{conv_round}_{extra_round}_7.png")


# varying number of convergence rounds
my_ZD_tournament(30, 20)
my_ZD_tournament(50, 20)
my_ZD_tournament(100, 20)
my_ZD_tournament(150, 20)

# varying number of extra rounds
my_ZD_tournament(150, 5)
my_ZD_tournament(150, 10)
my_ZD_tournament(150, 30)
my_ZD_tournament(150, 40)
