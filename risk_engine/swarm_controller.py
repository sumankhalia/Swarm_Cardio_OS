from agents.strategy_agent import StrategyAgent
from agents.risk_agent import RiskAgent
from agents.stability_agent import StabilityAgent
from agents.governance_agent import GovernanceAgent
from agents.skeptic_agent import SkepticAgent
from agents.instability_agent import InstabilityAgent
from agents.early_warning_agent import EarlyWarningAgent

from risk_engine.probabilistic_model import ProbabilisticRisk


class SwarmController:

    @staticmethod
    def run(signals):

        # Agent Evaluations
        strategy_score, strategy_reasoning = StrategyAgent.evaluate(signals)
        risk_score, risk_reasoning = RiskAgent.evaluate(signals)
        stability_score, stability_reasoning = StabilityAgent.evaluate(signals)
        governance_score, governance_reasoning = GovernanceAgent.evaluate(signals)

        skeptic_pressure, skeptic_reasoning = SkepticAgent.evaluate(
            strategy_score, risk_score
        )

        instability_reasoning = InstabilityAgent.evaluate(signals)
        early_warning_reasoning = EarlyWarningAgent.evaluate(signals)

        # Composite Swarm Intelligence Score
        composite = (
            strategy_score * 0.25
            + stability_score * 0.25
            + governance_score * 0.2
            - risk_score * 0.3
            - skeptic_pressure * 0.1
        )

        # Probabilistic Risk Layer
        risk_probability = ProbabilisticRisk.compute(composite)

        # Decision Logic
        if composite < 2:
            decision = "High Risk – Clinical Attention Recommended"
        elif composite < 5:
            decision = "Moderate Risk – Monitor & Stabilize"
        else:
            decision = "Stable Condition"

        # Structured Output (Enterprise Friendly)
        return {

            "Decision": decision,
            "CompositeScore": round(composite, 2),
            "RiskProbability": risk_probability,

            "Agents": {

                "StrategyAgent": {
                    "score": round(strategy_score, 2),
                    "reasoning": strategy_reasoning,
                },

                "RiskAgent": {
                    "score": round(risk_score, 2),
                    "reasoning": risk_reasoning,
                },

                "StabilityAgent": {
                    "score": round(stability_score, 2),
                    "reasoning": stability_reasoning,
                },

                "GovernanceAgent": {
                    "score": round(governance_score, 2),
                    "reasoning": governance_reasoning,
                },

                "SkepticAgent": {
                    "pressure": round(skeptic_pressure, 2),
                    "reasoning": skeptic_reasoning,
                },

                "InstabilityAgent": instability_reasoning,
                "EarlyWarningAgent": early_warning_reasoning,
            }
        }
