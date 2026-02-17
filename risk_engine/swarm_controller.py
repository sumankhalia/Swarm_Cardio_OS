from agents.strategy_agent import StrategyAgent
from agents.risk_agent import RiskAgent
from agents.stability_agent import StabilityAgent
from agents.instability_agent import InstabilityAgent
from agents.governance_agent import GovernanceAgent
from agents.trend_agent import TrendAgent

from agents.skeptic_agent import SkepticAgent
from agents.early_warning_agent import EarlyWarningAgent
from agents.crisis_prediction_agent import CrisisPredictionAgent

from agents.patient_regulation_agent import PatientRegulationAgent

import statistics
import math


class SwarmController:

    @staticmethod
    def run(signals, deviations):

        composite_score = (
            signals["cardiac_load"] * 0.35
            + signals["recovery_deficit"] * 0.25
            + signals["autonomic_instability"] * 0.25
            + signals["variability_risk"] * 0.15
        )

        risk_probability = 1 / (1 + math.exp(-composite_score / 10))

        agents_output = {

            # Core swarm cognition
            "StrategyAgent": StrategyAgent.evaluate(signals, composite_score),
            "RiskAgent": RiskAgent.evaluate(signals, composite_score),
            "StabilityAgent": StabilityAgent.evaluate(signals, composite_score),
            "InstabilityAgent": InstabilityAgent.evaluate(signals, composite_score),
            "GovernanceAgent": GovernanceAgent.evaluate(signals, composite_score),
            "TrendAgent": TrendAgent.evaluate(signals, deviations),

            # Meta cognition layer
            "SkepticAgent": SkepticAgent.evaluate(signals, composite_score),
            "EarlyWarningAgent": EarlyWarningAgent.evaluate(signals, deviations),
            "CrisisPredictionAgent": CrisisPredictionAgent.evaluate(signals, deviations),

            # Regulation layer
            "PatientRegulationAgent": PatientRegulationAgent.evaluate(
                signals, composite_score
            ),
        }

        confidences = []

        for agent in agents_output.values():
            if "confidence" in agent:
                confidences.append(agent["confidence"])

        consensus_confidence = statistics.mean(confidences)
        dispersion = statistics.pstdev(confidences)

        if risk_probability > 0.75:
            decision = "High Risk – Clinical Attention Recommended"
        elif risk_probability > 0.45:
            decision = "Moderate Instability – Monitor Trends"
        else:
            decision = "Stable Adaptive State"

        return {
            "Decision": decision,
            "CompositeScore": round(composite_score, 2),
            "RiskProbability": round(risk_probability, 3),
            "Consensus": {
                "summary": (
                    "Emerging instability patterns detected"
                    if risk_probability > 0.45
                    else "System signals remain within adaptive tolerance"
                ),
                "confidence": round(consensus_confidence, 2),
            },
            "Agents": agents_output,
            "MetaAnalysis": {
                "dispersion": round(dispersion, 2)
            },
        }
