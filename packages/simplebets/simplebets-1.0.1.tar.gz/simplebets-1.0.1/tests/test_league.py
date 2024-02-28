import unittest
from simplebets.league import SupportedLeagues

class TestLeague(unittest.TestCase):
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
        result = SupportedLeagues.as_list()
        expected = ["NBA"]
        self.assertEqual(result, expected)

    

