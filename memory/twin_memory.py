class TwinMemory:

    def __init__(self):
        self.history = []

    def store(self, signals):
        self.history.append(signals)

    def baseline(self):

        if not self.history:
            return {}

        baseline = {}

        keys = self.history[0].keys()

        for key in keys:

            values = []

            for h in self.history:
                value = h.get(key)

                if isinstance(value, (int, float)):
                    values.append(value)

            if len(values) == 0:
                continue   # 🔥 HARD SAFETY FIX

            baseline[key] = sum(values) / len(values)

        return baseline

    def deviation(self, latest):

        base = self.baseline()

        if not base:
            return {}

        deviation = {}

        for key, base_value in base.items():

            value = latest.get(key)

            if isinstance(value, (int, float)):
                deviation[key] = value - base_value

        return deviation
