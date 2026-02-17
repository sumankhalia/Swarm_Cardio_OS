class WhatIfEngine:

    @staticmethod
    def apply_intervention(signals, scenario):

        modified = signals.copy()

        if scenario == "improved_sleep":
            modified["sleep_quality"] += 1.5
            modified["recovery_deficit"] -= 0.8

        elif scenario == "high_stress":
            modified["stress_index"] += 2
            modified["autonomic_instability"] += 1

        elif scenario == "bp_spike":
            modified["hemodynamic_strain"] += 1.5
            modified["cardiac_load"] += 1

        return modified
