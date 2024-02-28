from statistics import NormalDist
from enum import Enum


class IndividualMetrics:
    def calculate_probability_of_metric_above_value(mu: float, sigma: float, value: float) -> float:
        return round(1 - NormalDist(mu=mu, sigma=sigma).cdf(value), 2)
    
    def calculate_probability_of_metric_under_equal_value(mu: float, sigma: float, value: float) -> float:
        return round(NormalDist(mu=mu, sigma=sigma).cdf(value), 2)