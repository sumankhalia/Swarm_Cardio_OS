import random
import math


class CardiacSyntheticGenerator:

    @staticmethod
    def generate_baseline():

        heart_rate = random.uniform(55, 85)
        hrv = random.uniform(40, 90)
        systolic_bp = random.uniform(105, 135)
        spo2 = random.uniform(96, 100)
        sleep_quality = random.uniform(6, 9)
        stress_index = random.uniform(2, 6)
        activity_level = random.uniform(4, 8)
        weight = random.uniform(60, 95)

        return {
            "heart_rate": heart_rate,
            "hrv_index": hrv,
            "blood_pressure": systolic_bp,
            "spo2": spo2,
            "sleep_quality": sleep_quality,
            "stress_index": stress_index,
            "activity_level": activity_level,
            "weight": weight,
        }

    @staticmethod
    def apply_deterioration(signals, severity):

        deterioration_factor = severity * random.uniform(0.8, 1.2)

        signals["heart_rate"] += deterioration_factor * random.uniform(1, 4)
        signals["hrv_index"] -= deterioration_factor * random.uniform(2, 6)
        signals["blood_pressure"] += deterioration_factor * random.uniform(0.5, 2)
        signals["sleep_quality"] -= deterioration_factor * random.uniform(0.3, 1.2)
        signals["stress_index"] += deterioration_factor * random.uniform(0.5, 2.5)
        signals["activity_level"] -= deterioration_factor * random.uniform(0.2, 1.5)
        signals["weight"] += deterioration_factor * random.uniform(0.05, 0.3)

        signals["spo2"] -= deterioration_factor * random.uniform(0.05, 0.3)

        return signals

    @staticmethod
    def baseline_drift(signals):

        signals["heart_rate"] += random.uniform(-1.5, 1.5)
        signals["hrv_index"] += random.uniform(-3, 3)
        signals["blood_pressure"] += random.uniform(-2, 2)
        signals["sleep_quality"] += random.uniform(-0.5, 0.5)
        signals["stress_index"] += random.uniform(-0.7, 0.7)
        signals["activity_level"] += random.uniform(-0.8, 0.8)
        signals["weight"] += random.uniform(-0.05, 0.05)
        signals["spo2"] += random.uniform(-0.1, 0.1)

        return signals

    @staticmethod
    def rare_event(signals):

        event_probability = random.random()

        if event_probability < 0.03:

            signals["heart_rate"] += random.uniform(15, 40)
            signals["hrv_index"] -= random.uniform(10, 25)
            signals["blood_pressure"] -= random.uniform(5, 20)
            signals["spo2"] -= random.uniform(1, 4)

            signals["event_flag"] = "Acute Cardiac Stress Event"

        elif event_probability < 0.06:

            signals["heart_rate"] += random.uniform(5, 15)
            signals["hrv_index"] -= random.uniform(5, 12)

            signals["event_flag"] = "Transient Instability"

        else:
            signals["event_flag"] = None

        return signals

    @staticmethod
    def inject_noise(signals):

        noise_scale = random.uniform(0.95, 1.05)

        noisy_signals = {}

        for key, value in signals.items():

            if isinstance(value, (int, float)):
                noisy_signals[key] = value * noise_scale
            else:
                noisy_signals[key] = value

        if random.random() < 0.05:
            noisy_signals["hrv_index"] *= random.uniform(0.7, 1.3)

        if random.random() < 0.04:
            noisy_signals["heart_rate"] += random.uniform(-8, 8)

        return noisy_signals

    @staticmethod
    def derive_cognitive_signals(signals):

        cardiac_load = (
            (signals["heart_rate"] / 100) * 4
            + (10 - signals["hrv_index"] / 10) * 3
            + (signals["blood_pressure"] / 150) * 3
        )

        recovery_deficit = (
            (10 - signals["sleep_quality"]) * 0.6
            + signals["stress_index"] * 0.4
        )

        autonomic_instability = (
            (10 - signals["hrv_index"] / 10) * 0.7
            + signals["stress_index"] * 0.3
        )

        hemodynamic_strain = signals["blood_pressure"] / 20

        variability_risk = abs(50 - signals["hrv_index"]) / 10

        fluid_retention_pressure = signals["weight"] / 20

        return {
            "sleep_quality": round(signals["sleep_quality"], 2),
            "stress_index": round(signals["stress_index"], 2),
            "cardiac_load": round(cardiac_load, 2),
            "recovery_deficit": round(recovery_deficit, 2),
            "autonomic_instability": round(autonomic_instability, 2),
            "hemodynamic_strain": round(hemodynamic_strain, 2),
            "variability_risk": round(variability_risk, 2),
            "fluid_retention_pressure": round(fluid_retention_pressure, 2),
            "event_flag": signals.get("event_flag"),
        }

    @staticmethod
    def generate_patient(months=12):

        signals = CardiacSyntheticGenerator.generate_baseline()

        history = []

        for month in range(months):

            severity = month / months

            signals = CardiacSyntheticGenerator.baseline_drift(signals)
            signals = CardiacSyntheticGenerator.apply_deterioration(signals, severity)
            signals = CardiacSyntheticGenerator.rare_event(signals)
            signals = CardiacSyntheticGenerator.inject_noise(signals)

            cognitive = CardiacSyntheticGenerator.derive_cognitive_signals(signals)

            history.append(cognitive)

        return history
