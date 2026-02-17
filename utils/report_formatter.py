class ReportFormatter:

    @staticmethod
    def normalize(agent):
        """
        Makes formatter immune to:
        ✔ wrapped agents
        ✔ raw agents
        ✔ partial outputs
        ✔ LLM failures
        """

        if not agent:
            return {
                "signal_assessment": "Unavailable",
                "risk_interpretation": "Unavailable",
                "confidence": 0
            }

        # Case 1 → Wrapped agent {score, reasoning}
        if "reasoning" in agent:
            reasoning = agent.get("reasoning", {})

        # Case 2 → Raw agent JSON
        else:
            reasoning = agent

        return {
            "signal_assessment": reasoning.get("signal_assessment", "Unavailable"),
            "risk_interpretation": reasoning.get("risk_interpretation", "Unavailable"),
            "confidence": reasoning.get("confidence", 0)
        }

    @staticmethod
    def format_for_ui(swarm_output):

        agents = swarm_output.get("Agents", {})

        return {
            "Decision": swarm_output.get("Decision"),
            "CompositeScore": swarm_output.get("CompositeScore"),
            "RiskProbability": swarm_output.get("RiskProbability"),

            "Consensus": swarm_output.get("Consensus", {}),

            "Agents": {
                name: ReportFormatter.normalize(agent)
                for name, agent in agents.items()
            },

            "MetaAnalysis": swarm_output.get("MetaAnalysis", {})
        }
