from enum import Enum
from typing import Optional, List

class SupportedMarkets(str, Enum):
    individual_metric_eq_under = "individual_metric_eq_under"
    individual_metric_over = "individual_metric_over"
    asian_handicap_under = "asian_handicap_under"
    asian_handicap_over = "asian_handicap_over"
    odd = "odd"
    even = "even"
    head_to_head = "head_to_head"

    def as_list() -> List[str]:
        return [e.value for e in SupportedMarkets]

class Market:
    market_name: str
    price: float
    participant_name: Optional[str]
    line: Optional[str]
    



