from data_pipeline.synthetic_generator import CardiacSyntheticGenerator
from risk_engine.swarm_controller import SwarmController
from risk_engine.debate_engine import DebateEngine
from memory.twin_memory import TwinMemory
from agents.crisis_prediction_agent import CrisisPredictionAgent
from utils.visualizer import Visualizer


def run_swarm():

    history = CardiacSyntheticGenerator.generate_patient(months=12)

    memory = TwinMemory()

    for state in history:
        memory.store(state)

    latest = history[-1]

    deviations = memory.deviation(latest)

    swarm_output = SwarmController.run(latest)

    consensus = DebateEngine.run_debate(swarm_output)

    crisis_forecast = CrisisPredictionAgent.evaluate(latest, deviations)

    return {
        "Decision": swarm_output["Decision"],
        "RiskProbability": swarm_output["RiskProbability"],
        "CompositeScore": swarm_output["CompositeScore"],
        "Agents": swarm_output["Agents"],
        "Debate": consensus,
        "CrisisForecast": crisis_forecast,
        "LatestState": latest,
        "Deviations": deviations
    }


def main():

    result = run_swarm()

    print("\nSWARM OUTPUT:")
    print(result)

    Visualizer.plot_history(
        CardiacSyntheticGenerator.generate_patient(months=12)
    )


if __name__ == "__main__":
    main()
