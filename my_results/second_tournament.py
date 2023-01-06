import axelrod as axl
import matplotlib.pyplot as plt

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
plt.savefig("second_axelrod_rankings_7.png")

plot.lengthplot()
plt.xlabel("Strategies")
plt.ylabel("Length of the matches")
plt.savefig("second_axelrod_length_7.png")
