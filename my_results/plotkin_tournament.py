import axelrod as axl
import matplotlib.pyplot as plt

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

# creating the tournament
tournament = axl.Tournament(
    players=players,
    turns=200,
    repetitions=5,
    seed=7,
    )
results = tournament.play()

# plot the rankings
plot = axl.Plot(results)
plot.boxplot()
plt.xlabel("Strategies")
plt.ylabel("Scores")
plt.savefig("plotkin_rankings_7.png")

