import axelrod as axl
import matplotlib.pyplot as plt

def first_tournament(seed):
    # getting the players for the first tournament
    first_tournament_participants_ordered_by_reported_rank = [s() for s in axl.axelrod_first_strategies]
    number_of_strategies = len(first_tournament_participants_ordered_by_reported_rank)

    # creating the tournament
    tournament = axl.Tournament(
        players=first_tournament_participants_ordered_by_reported_rank,
        turns=200,
        repetitions=5,
        seed=seed,
        )
    results = tournament.play()

    # plot the rankings
    plot = axl.Plot(results)
    plot.boxplot()
    plt.xlabel("Strategies")
    plt.ylabel("Scores")
    plt.savefig(f"first_axelrod_rankings_{seed}.png")

    # plot the reported ranks vs the reduced ranks
    plt.figure(figsize=(15, 6)) 
    plt.plot((0, 15), (0, 15), color="grey", linestyle="--")  
    for original_rank, strategy in enumerate(first_tournament_participants_ordered_by_reported_rank):
        rank = results.ranked_names.index(str(strategy))
        if rank == original_rank:
            symbol = "+"
            plt.plot((rank, rank), (rank, 0), color="grey")
        else:
            symbol = "o"
            plt.scatter([rank], [original_rank], marker=symbol, color="red", s=50)  
            plt.xticks(range(number_of_strategies), results.ranked_names, rotation=90)  

    plt.ylabel("Reported rank")
    plt.xlabel("Reproduced rank")
    plt.savefig(f"first_tournament_reported_vs_reproduced_{seed}.png")

# play the tournament for a different seeds


first_tournament(1)
first_tournament(10)
first_tournament(7)
# take seed 7 in the future
