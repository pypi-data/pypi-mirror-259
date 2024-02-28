import unittest
from simplebets.bet import Bet
from simplebets.market import SupportedMarkets
from simplebets.league import SupportedLeagues
from simplebets.participant import Participant

class TestBet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass
    
    def test_init(self) -> None:
        participants = [Participant(participant_name = "Stephen Curry")]
        bet = Bet(
            fixture_id=123, 
            market=SupportedMarkets.individual_metric_over.value,
            league=SupportedLeagues.NBA.value,
            participants=participants,
            metric="points",
            metric_value=30
            )
        self.assertEqual(isinstance(bet, Bet), True)

    def test_init_head_to_head(self) -> None:
        participants = [
            Participant(participant_name = "GSW", participant_location="1"),
            Participant(participant_name = "PHX", participant_location="2"),
        ]
        bet = Bet(
            fixture_id=123, 
            market=SupportedMarkets.head_to_head.value,
            league=SupportedLeagues.NBA.value,
            participants=participants,
            )
        self.assertEqual(isinstance(bet, Bet), True)

    def test_not_supported_market(self) -> None:
        participants = [Participant(participant_name = "Stephen Curry")]
        with self.assertRaises(Exception):
            bet = Bet(
                fixture_id=123, 
                market="wrongmarket",
                league=SupportedLeagues.NBA.value,
                participants=participants,
                metric="points",
                metric_value=30
                )      
            
    def test_not_supported_league(self) -> None:
        participants = [Participant(participant_name = "Stephen Curry")]
        with self.assertRaises(Exception):
            bet = Bet(
                fixture_id=123, 
                market=SupportedMarkets.individual_metric_over.value,
                league="wrongleague",
                participants=participants,
                metric="points",
                metric_value=30
                )               
    

