import unittest
import os
from simplebets.individual_metrics import IndividualMetrics

class TestIndividualMetrics(unittest.TestCase):
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

    def test_individual_metrics(self) -> None:
        mu = 20
        sigma = 5
        result = IndividualMetrics.calculate_probability_of_metric_above_value(mu=mu, sigma=sigma, value=mu+sigma)
        self.assertEqual(result, 0.16)

        result = IndividualMetrics.calculate_probability_of_metric_under_equal_value(mu=mu, sigma=sigma, value=mu+sigma)
        self.assertEqual(result, 0.84)