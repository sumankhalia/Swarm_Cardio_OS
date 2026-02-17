from data_pipeline.synthetic_generator import CardiacSyntheticGenerator
from risk_engine.swarm_controller import SwarmController
from memory.twin_memory import TwinMemory
from utils.report_formatter import ReportFormatter
from utils.pdf_report import generate_pdf_report


def run_swarm():

    history = CardiacSyntheticGenerator.generate_patient(months=12)

    memory = TwinMemory()

    for state in history:
        memory.store(state)

    latest = history[-1]

    deviations = memory.deviation(latest)

    swarm_output = SwarmController.run(latest, deviations)

    formatted_report = ReportFormatter.format_for_ui(swarm_output)

    generate_pdf_report(formatted_report)

    return formatted_report


def main():

    result = run_swarm()

    print("\nCARDIOSPHERE INTELLIGENCE OUTPUT")
    print("--------------------------------------------------")

    print(f"\nDecision: {result.get('Decision')}")
    print(f"Composite Score: {round(result.get('CompositeScore', 0), 2)}")
    print(f"Risk Probability: {round(result.get('RiskProbability', 0), 3)}")

    print("\nConsensus Analysis")
    print("--------------------------------------------------")

    consensus = result.get("Consensus", {})

    print(consensus.get("summary", "Unavailable"))
    print(f"Confidence Level: {round(consensus.get('confidence', 0), 2)}")

    print("\nAgent Interpretations")
    print("--------------------------------------------------")

    for agent_name, agent_data in result.get("Agents", {}).items():

        print(f"\n{agent_name}")
        print(agent_data.get("signal_assessment", "Unavailable"))
        print(agent_data.get("risk_interpretation", "Unavailable"))
        print(f"Confidence: {agent_data.get('confidence', 0)}")

    print("\nMeta Analysis")
    print("--------------------------------------------------")

    meta = result.get("MetaAnalysis", {})

    print(f"Cognitive Dispersion: {round(meta.get('dispersion', 0), 2)}")


if __name__ == "__main__":
    main()
