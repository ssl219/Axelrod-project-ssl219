from typing import List

from axelrod.action import Action
from axelrod.player import Player
import numpy as np
import statsmodels.api as sm

C, D = Action.C, Action.D


class Adaptive(Player):
    """Start with a specific sequence of C and D, then play the strategy that
    has worked best, recalculated each turn.

    Names:

    - Adaptive: [Li2011]_

    """

    name = "Adaptive"
    classifier = {
        "memory_depth": float("inf"),  # Long memory
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, initial_plays: List[Action] = None) -> None:
        super().__init__()
        if not initial_plays:
            initial_plays = [C] * 6 + [D] * 5
        self.initial_plays = initial_plays
        self.scores = {C: 0, D: 0}

    def score_last_round(self, opponent: Player):
        # Load the default game if not supplied by a tournament.
        game = self.match_attributes["game"]
        if len(self.history):
            last_round = (self.history[-1], opponent.history[-1])
            scores = game.score(last_round)
            self.scores[last_round[0]] += scores[0]

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        # Update scores from the last play
        self.score_last_round(opponent)
        # Begin by playing the sequence C,C,C,C,C,C,D,D,D,D,D
        index = len(self.history)
        if index < len(self.initial_plays):
            return self.initial_plays[index]
        # Play the strategy with the highest average score so far
        if self.scores[C] > self.scores[D]:
            return C
        return D

class ZDAdaptive(Adaptive):
    """Start with a specific sequence of C and D, then play the strategy that
    has worked best, recalculated each turn. Also has a theory of mind similar 
    to ZD TitForTat.

    Names:

    - ZDAdaptive: Selena Linden

    """

    name = "ZDAdaptive"
    classifier = {
        "memory_depth": float("inf"),  # Long memory
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, conv_round, extra_round, initial_plays: List[Action] = None) -> None:
        super().__init__()
        self.conv_round = conv_round
        self.extra_round = extra_round
        self.sx = np.zeros(200-conv_round)
        self.sy = np.zeros(200-conv_round)
        self.allD = False
        self.whenallD = "Never"


    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        """This is the actual strategy"""
        # Update scores from the last play
        self.score_last_round(opponent)
        # Begin by playing the sequence C,C,C,C,C,C,D,D,D,D,D
        index = len(self.history)
        if index < len(self.initial_plays):
            return self.initial_plays[index]

        # If we have already reverted to Always Defect strategy, defect
        if self.allD:
            return D
        if len(self.history) == 199:
            print(self.whenallD)

        if len(self.history) >= self.conv_round:
            # calculate the last round's scores and append to the vectors
            if self.history[-1] == C:
                if opponent.history[-1] == C:
                    score_x = 3
                    score_y = 3
                else:
                    score_x = 0
                    score_y = 5
            else:
                if opponent.history[-1] == C:
                    score_x = 5
                    score_y = 0
                else:
                    score_x = 1
                    score_y = 1
            self.sx[len(self.history)-self.conv_round] = score_x
            self.sy[len(self.history)-self.conv_round] = score_y

        if (len(self.history) - self.conv_round) % self.extra_round == 0:
            if len(self.history) > self.conv_round:
                # fit linear regression to determine if opponent is playing ZD
                # define predictor and response variables
                resp = self.sx[:len(self.history)]
                pred = self.sy[:len(self.history)]
                # add constant to predictor variables
                pred = sm.add_constant(pred)
                # fit the linear regression model
                model = sm.OLS(resp, pred).fit()
                # extract p-value corresponding to the coefficient of pred
                p_val = model.pvalues[1]
                # print(f"P-value at round {len(self.history)}:", p_val)
                # extract adjusted R squared
                r_squared = model.rsquared_adj
                # print(f"R-squared at round {len(self.history)}:", r_squared)
                # if linear relationship is significant at the 1% significance
                # level and adjusted R squared is close to 1 or -1, then 
                # revert to always defect strategy
                if p_val < 0.01 and abs(1-r_squared) < 0.8:
                    self.allD = True
                    self.whenallD = len(self.history)
                    # print("yes!")      
        # if linear relationship is not significant, continue playing TFT
        if not self.allD:
            # Play the strategy with the highest average score so far
            if self.scores[C] > self.scores[D]:
                return C
            else:
                return D
        # if linear relationship is significant, defect
        else:
            return D
        
