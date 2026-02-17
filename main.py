from data_pipeline.synthetic_generator import CardiacSyntheticGenerator
from risk_engine.swarm_controller import SwarmController
from risk_engine.debate_engine import DebateEngine
from memory.twin_memory import TwinMemory
from agents.crisis_prediction_agent import CrisisPredictionAgent
from utils.visualizer import Visualizer


def main():

    history = CardiacSyntheticGenerator.generate_patient(months=12)

    memory = TwinMemory()

    for state in history:
        memory.store(state)

    latest = history[-1]

    deviations = memory.deviation(latest)

    swarm_output = SwarmController.run(latest)

    consensus = DebateEngine.run_debate(swarm_output)

    crisis_forecast = CrisisPredictionAgent.evaluate(latest, deviations)

    print("\nSWARM OUTPUT:")
    print(swarm_output)

    print("\nDEBATE CONSENSUS:")
    print(consensus)

    print("\nCRISIS FORECAST:")
    print(crisis_forecast)

    Visualizer.plot_history(history)


if __name__ == "__main__":
    main()
