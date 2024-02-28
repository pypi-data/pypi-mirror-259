import unittest
from simplebets.market import Market, SupportedMarkets

class TestMarket(unittest.TestCase):
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
    
    def test_to_list(self) -> None:
        result = SupportedMarkets.as_list()
        expected = [
            'individual_metric_eq_under', 
            'individual_metric_over', 
            'asian_handicap_under', 
            'asian_handicap_over', 
            'odd', 
            'even', 
            'head_to_head'
        ]
        self.assertEqual(result, expected)

    

