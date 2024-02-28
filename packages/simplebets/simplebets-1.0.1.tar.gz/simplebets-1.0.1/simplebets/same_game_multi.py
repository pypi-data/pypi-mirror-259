from typing import List
from simplebets.bet import Bet
import itertools

class SameGameMulti:
    bets: List[Bet]

    def __init__(self, bets: List[Bet]) -> None:
        """
        `SameGameMulti`: this class was written with the intention of passing
        a betslip (series of bets), and determining the odds for that bet
        It should be capable of understanding the relationship between individual bets in the bet slip,
        ie. Whether bets are independent or dependent and the degree to which they are related, 
        this should be factored in prior to returning the odds
        """
        self.bets = bets
        self.odds = self.get_odds(bets = bets)

    def get_odds(self, bets: List[Bet]) -> float:
        # grouped_bets = itertools.groupby(bets, lambda bet: bet.fixture_id)
        # for fixture_id, fixture_bets in grouped_bets:
        #     for bet in fixture_bets:
        pass

    