class AdaptiveBaseline:

    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.baseline = {}

    def update(self, signals):

        for key, value in signals.items():

            if not isinstance(value, (int, float)):
                continue

            if key not in self.baseline:
                self.baseline[key] = value
            else:
                self.baseline[key] = (
                    self.alpha * value
                    + (1 - self.alpha) * self.baseline[key]
                )

    def deviation(self, signals):

        deviations = {}

        for key, value in signals.items():

            if key in self.baseline and isinstance(value, (int, float)):
                deviations[key] = value - self.baseline[key]

        return deviations
