from dataclasses import dataclass
from typing import List, Optional
from simplebets.participant import Participant
from simplebets.market import SupportedMarkets
from simplebets.league import SupportedLeagues

class Bet:
    fixture_id: str
    market: str
    league: str
    participants: List[Participant]
    metric: Optional[str]
    metric_value: Optional[str]

    def __init__(self, 
            fixture_id: str, 
            market: str, 
            league: str, 
            participants: List[Participant], 
            metric: Optional[str] = None,
            metric_value: Optional[str] = None) -> None:
        self.fixture_id = fixture_id
        self.market = self.set_market(market = market)
        self.league = self.set_league(league = league)
        self.participants = participants
        self.metric = metric
        self.metric_value = metric_value
    
    def set_market(self, market: str):
        if market not in list(SupportedMarkets):
            raise Exception(f"We do not support market: {market}")
        
    def set_league(self, league: str):
        if league not in list(SupportedLeagues):
            raise Exception(f"We do not support market: {league}")        
        


