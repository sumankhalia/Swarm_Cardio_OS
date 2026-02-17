class DebateEngine:

    @staticmethod
    def run_debate(swarm_output):

        agents = swarm_output.get("Agents", {})

        scores = []

        for agent in agents.values():
            if "score" in agent:
                scores.append(agent["score"])

        if not scores:
            return {"summary": "No agent consensus available"}

        avg_score = sum(scores) / len(scores)

        if avg_score < 10:
            stance = "System signals remain within adaptive tolerance"

        elif avg_score < 18:
            stance = "Emerging instability patterns detected"

        else:
            stance = "High-risk convergence across agents"

        return {
            "summary": stance,
            "confidence": round(avg_score, 2)
        }
