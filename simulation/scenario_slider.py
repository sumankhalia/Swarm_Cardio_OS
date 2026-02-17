class ScenarioSlider:

    @staticmethod
    def apply_load(signals, intensity):

        adjusted = signals.copy()

        factor = intensity / 10

        adjusted["cardiac_load"] *= (1 + factor)
        adjusted["recovery_deficit"] *= (1 + factor)
        adjusted["autonomic_instability"] *= (1 + factor)

        return adjusted
