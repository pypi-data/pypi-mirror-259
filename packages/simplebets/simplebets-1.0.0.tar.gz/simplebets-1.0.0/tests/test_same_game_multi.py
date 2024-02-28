import unittest
import itertools
from enum import Enum
class MockSupportedLeagues(str, Enum):
    NBA = "NBA"
    # NBL = "NBL"
    # NFL = "NFL"
    # AFL = "AFL"

class FakeBet:
    def __init__(self, fixture_id: str) -> None:
        self.fixture_id = fixture_id

class TestSGM(unittest.TestCase):
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
    
    def test_sgm_list(self) -> None:
        bets = [FakeBet(fixture_id=4), FakeBet(fixture_id=2), FakeBet(fixture_id=1), FakeBet(fixture_id=1)]
        group_by = itertools.groupby(bets, lambda bet: bet.fixture_id)
        for k, g in group_by:
            print(k, list(g))

    

