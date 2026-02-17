import math


class ProbabilisticRisk:

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    @staticmethod
    def compute(composite_score):

        probability = ProbabilisticRisk.sigmoid(5 - composite_score)

        return round(probability, 3)
