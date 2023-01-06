import axelrod as axl
import matplotlib.pyplot as plt
from axelrod.strategies.titfortat import ZDTitForTat
from axelrod.strategies.adaptive import ZDAdaptive


def my_second_tournament(conv_round, extra_round):
    players = [
        axl.TitForTat(), 
        axl.Grudger(),
        axl.GoByMajority(),
        axl.SecondByKluepfel(),
        axl.SecondByWeiner(),
        axl.SecondByBorufsen(),
        axl.SecondByWmAdams(),
        axl.SecondByEatherley(),
        axl.SecondByRichardHufford(),
        axl.SecondByCave(),
        axl.SecondByRowsam(),
        axl.RevisedDowning(),
        axl.SecondByGraaskampKatzen(),
        axl.SecondByChampion(),
        axl.SecondByYamachi(),
        axl.SecondByTranquilizer(),
        axl.SecondByLeyvraz(),
        axl.SecondByWhite(),
        axl.SecondByHarrington(),
        axl.SecondByGladstein(),
        axl.SecondByWhite(),
        axl.SecondByTidemanAndChieruzzi(),
        axl.SecondByAppold(),
        axl.TitFor2Tats(),
        axl.WinStayLoseShift(),
        axl.Random(),
        ]
    
    players = players + [ZDTitForTat(conv_round, extra_round), ZDAdaptive(conv_round, extra_round)]
    # creating the tournament
    tournament = axl.Tournament(
        players=players,
        turns=200,
        repetitions=5,
        seed=7,
        prob_end=0.00346
        )
    results = tournament.play()

    # plot the rankings
    plot = axl.Plot(results)
    plot.boxplot()
    plt.xlabel("Strategies")
    plt.ylabel("Scores")
    plt.savefig(f"my_second_rankings_{conv_round}_{extra_round}_7.png")

    plot.lengthplot()
    plt.xlabel("Strategies")
    plt.ylabel("Length of the matches")
    plt.savefig(f"my_second_lengths_{conv_round}_{extra_round}_7.png")

# varying number of convergence rounds
my_second_tournament(30, 20)
my_second_tournament(50, 20)
my_second_tournament(100, 20)
my_second_tournament(150, 20)

# varying number of extra rounds
my_second_tournament(150, 5)
my_second_tournament(150, 10)
my_second_tournament(150, 30)
my_second_tournament(150, 40)