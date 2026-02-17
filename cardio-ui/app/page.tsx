"use client";

import { useState } from "react";

const agentsInfo: Record<string, string> = {
  StrategyAgent: "System-level interpreter of physiological state and adaptive dynamics",
  RiskAgent: "Quantifies vulnerability, destabilization probability, and exposure intensity",
  StabilityAgent: "Evaluates resilience, buffering capacity, and recovery balance",
  InstabilityAgent: "Detects strain accumulation, deterioration patterns, collapse signals",
  GovernanceAgent: "Assesses regulatory balance, control priorities, intervention necessity",
  TrendAgent: "Analyzes deviation dynamics, trajectory shifts, temporal drift patterns",
  SkepticAgent: "Challenges assumptions, detects contradictions, evaluates uncertainty",
  EarlyWarningAgent: "Identifies emerging risk signals before instability thresholds",
  CrisisPredictionAgent: "Estimates near-term destabilization probability from deviations",
  PatientRegulationAgent: "Generates adaptive behavioral guidance for stability and recovery",
};

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState<any>(null);

  const [inputs, setInputs] = useState({
    sleep_quality: 5,
    stress_index: 5,
    cardiac_load: 5,
    recovery_deficit: 5,
    autonomic_instability: 5,
  });

  const handleChange = (key: string, value: number) => {
    setInputs({ ...inputs, [key]: value });
  };

  const runSwarm = async () => {
    setLoading(true);
    setReport(null);

    try {
      const res = await fetch("https://swarm-cardio-os.onrender.com/analyze");
      const data = await res.json();
      setReport(data);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Aether Cardiac Intelligence</h1>

      <div className={`heart ${loading ? "spin" : ""}`} />

      <button onClick={runSwarm}>
        {loading ? "Analyzing Cognitive Signals..." : "Analyze"}
      </button>

      {/* INPUT SIGNAL BARS */}
      <div className="inputs">
        <h2>Physiological Signal Inputs</h2>

        {Object.entries(inputs).map(([key, value]) => (
          <div key={key} className="inputRow">
            <label>{key.replace("_", " ")}</label>
            <input
              type="range"
              min="0"
              max="10"
              value={value}
              onChange={(e) =>
                handleChange(key, Number(e.target.value))
              }
            />
            <span>{value}</span>
          </div>
        ))}
      </div>

      {/* REPORT */}
      {report && (
        <div className="report">
          <h2>System Intelligence Assessment</h2>

          <div className="summary">
            <p><strong>Decision</strong> {report.Decision}</p>
            <p><strong>Composite Score</strong> {report.CompositeScore}</p>
            <p><strong>Risk Probability</strong> {report.RiskProbability}</p>
          </div>

          <h3>Multi-Agent Cognitive Interpretations</h3>

          {Object.entries(report.Agents).map(([name, agent]: any) => (
            <div key={name} className="agentCard">
              <div className="agentHeader">
                <span>{name}</span>
                <span
                  className="info"
                  title={agentsInfo[name]}
                >
                  ⓘ
                </span>
              </div>

              <div className="agentBody">
                <p>{agent.signal_assessment}</p>
                <p>{agent.risk_interpretation}</p>
              </div>

              <div className="confidence">
                Confidence Level {agent.confidence}
              </div>
            </div>
          ))}

          <div className="disclaimer">
            Aether Cardiac Intelligence is a multi-agentic AI cognitive system.
            Outputs represent computational interpretations of physiological signals
            and are not medical diagnosis or clinical advice.
          </div>
        </div>
      )}

      <style jsx>{`
        .container {
          background: linear-gradient(135deg, #020617, #0f172a);
          min-height: 100vh;
          color: white;
          text-align: center;
          padding: 50px;
          font-family: system-ui;
        }

        h1 {
          font-size: 46px;
          margin-bottom: 35px;
          color: #93c5fd;
          font-weight: 300;
          letter-spacing: 1px;
        }

        .heart {
          width: 150px;
          height: 150px;
          margin: 35px auto;
          border-radius: 50%;
          background: rgba(59, 130, 246, 0.18);
          backdrop-filter: blur(20px);
          box-shadow: 0 0 60px rgba(59, 130, 246, 0.35);
          transition: transform 1s ease;
        }

        .spin {
          animation: rotate 2.2s linear infinite;
        }

        @keyframes rotate {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }

        button {
          background: rgba(59, 130, 246, 0.28);
          border: 1px solid rgba(148, 163, 184, 0.2);
          padding: 14px 36px;
          border-radius: 30px;
          color: white;
          cursor: pointer;
          font-size: 18px;
          backdrop-filter: blur(10px);
          transition: all 0.3s ease;
        }

        button:hover {
          background: rgba(59, 130, 246, 0.4);
        }

        .inputs {
          max-width: 540px;
          margin: 50px auto;
          text-align: left;
          background: rgba(15, 23, 42, 0.5);
          padding: 25px;
          border-radius: 18px;
          backdrop-filter: blur(18px);
        }

        h2 {
          text-align: center;
          color: #60a5fa;
          font-weight: 400;
          margin-bottom: 25px;
        }

        .inputRow {
          display: flex;
          align-items: center;
          margin-bottom: 16px;
          gap: 12px;
        }

        label {
          width: 160px;
          font-size: 14px;
          color: #cbd5f5;
        }

        input[type="range"] {
          flex: 1;
        }

        .report {
          margin-top: 60px;
          background: rgba(15, 23, 42, 0.55);
          padding: 35px;
          border-radius: 24px;
          backdrop-filter: blur(25px);
          text-align: left;
          max-width: 900px;
          margin-left: auto;
          margin-right: auto;
        }

        h3 {
          margin-top: 30px;
          color: #93c5fd;
          font-weight: 400;
        }

        .agentCard {
          margin-top: 18px;
          padding: 18px;
          background: rgba(30, 41, 59, 0.6);
          border-radius: 14px;
        }

        .agentHeader {
          display: flex;
          justify-content: space-between;
          font-weight: 500;
          color: #bfdbfe;
          margin-bottom: 8px;
        }

        .agentBody p {
          margin: 4px 0;
          color: #e2e8f0;
          font-size: 14px;
        }

        .confidence {
          margin-top: 8px;
          font-size: 13px;
          color: #60a5fa;
        }

        .disclaimer {
          margin-top: 35px;
          font-size: 12px;
          color: #94a3b8;
          text-align: center;
        }

        .info {
          cursor: pointer;
          opacity: 0.6;
        }

        .info:hover {
          opacity: 1;
        }
      `}</style>
    </div>
  );
}
