from typing import List
import itertools
import trueskill
from trueskill import Rating
import math

class SimpleH2H:  
    def set_head_to_head_odds(bet: float) -> float:
        min_bet = 1.01
        max_bet = 10.00
        if bet < min_bet:
            return min_bet
        if bet > max_bet:
            return max_bet
        return bet
        
    def add_margin(probability: float) -> float:
        margin = 0.025
        return probability + margin

    def team_win_probability(home_team: List[Rating], away_team: List[Rating]):
        delta_mu = sum(rating.mu for rating in home_team) - sum(rating.mu for rating in away_team)
        sum_sigma = sum(rating.sigma ** 2 for rating in itertools.chain(home_team, away_team))
        size = len(home_team) + len(away_team)
        denom = math.sqrt(size * (trueskill.BETA * trueskill.BETA) + sum_sigma)
        ts = trueskill.TrueSkill(draw_probability=0.0)
        return round(ts.cdf(delta_mu / denom), 4)
    
    def get_odds_from_teams(team_1: List[Rating], team_2: List[Rating]) -> float:
        team_1_odds = SimpleH2H.set_head_to_head_odds( 1 / SimpleH2H.add_margin(SimpleH2H.team_win_probability(home_team=team_1, away_team=team_2)))
        return round(team_1_odds, 4)