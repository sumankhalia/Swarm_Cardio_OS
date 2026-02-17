class DebateEngine:

    @staticmethod
    def run_debate(agent_outputs):

        agents = agent_outputs.get("Agents", {})

        strategy_reasoning = agents.get("StrategyAgent", {}).get(
            "reasoning", "No reasoning available"
        )

        risk_reasoning = agents.get("RiskAgent", {}).get(
            "reasoning", "No reasoning available"
        )

        instability_reasoning = agents.get("InstabilityAgent", "No reasoning available")

        warning_reasoning = agents.get("EarlyWarningAgent", "No reasoning available")

        debate = f"""

STRATEGY AGENT PERSPECTIVE
{strategy_reasoning}

RISK AGENT PERSPECTIVE
{risk_reasoning}

INSTABILITY AGENT PERSPECTIVE
{instability_reasoning}

EARLY WARNING AGENT PERSPECTIVE
{warning_reasoning}

EXECUTIVE CONSENSUS
Integrated multi-agent reasoning synthesis complete.

"""

        return debate
