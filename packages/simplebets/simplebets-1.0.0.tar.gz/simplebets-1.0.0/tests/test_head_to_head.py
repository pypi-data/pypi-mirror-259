import unittest
from trueskill import Rating
from simplebets.head_to_head import SimpleH2H

class TestHeadtoHead(unittest.TestCase):
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
    
    def test_h2h_set_head_to_head_odds(self) -> None:
        result = SimpleH2H.set_head_to_head_odds(bet = 1.00)
        self.assertEqual(result, 1.01)

        result = SimpleH2H.set_head_to_head_odds(bet = 100.00)
        self.assertEqual(result, 10.00)

    def test_h2h_add_margin(self) -> None:
        result = SimpleH2H.add_margin(probability = 0.1)
        self.assertEqual(result, 0.125)

    def test_get_team_win_probability(self) -> None:
        team_1 = [Rating() for _ in range(8)]
        team_2 = [Rating() for _ in range(8)]
        result = SimpleH2H.team_win_probability(home_team = team_1, away_team = team_2)
        self.assertEqual(result, 0.5)

    def test_get_odds_from_teams(self) -> None:
        team_1 = [Rating() for _ in range(8)]
        team_2 = [Rating() for _ in range(8)]
        result = SimpleH2H.get_odds_from_teams(team_1 = team_1, team_2 = team_2)
        self.assertEqual(result, 1.9048)

        result = SimpleH2H.get_odds_from_teams(team_1 = team_2, team_2 = team_1)
        self.assertEqual(result, 1.9048)
    

