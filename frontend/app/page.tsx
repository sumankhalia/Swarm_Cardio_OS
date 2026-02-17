"use client";

import { useState } from "react";

export default function Home() {

  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState<any>(null);

  const runSwarm = async () => {
    setLoading(true);

    const res = await fetch("https://swarm-cardio-os.onrender.com/analyze");
    const data = await res.json();

    setReport(data);
    setLoading(false);
  };

  return (
    <main style={styles.container}>

      <h1 style={styles.title}>
        CardioSphere Intelligence
      </h1>

      <div style={{
        ...styles.sphere,
        ...(loading ? styles.pulse : {})
      }} />

      <button onClick={runSwarm} style={styles.button}>
        {loading ? "Swarm Thinking..." : "Run Swarm Engine"}
      </button>

      {report && (
        <div style={styles.report}>

          <h2 style={styles.heading}>Decision Overview</h2>
          <p style={styles.text}>{report.Decision}</p>

          <h2 style={styles.heading}>Risk Probability</h2>
          <p style={styles.text}>{report.RiskProbability}</p>

          <h2 style={styles.heading}>Composite Score</h2>
          <p style={styles.text}>{report.CompositeScore}</p>

        </div>
      )}

    </main>
  );
}

const styles: any = {

  container: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    minHeight: "100vh",
    background: "#f9fbfd",
    fontFamily: "sans-serif"
  },

  title: {
    fontWeight: 300,
    marginBottom: 40
  },

  sphere: {
    width: 140,
    height: 140,
    borderRadius: "50%",
    background: "linear-gradient(135deg, #89CFF0, #6FAED9)",
    marginBottom: 30,
    transition: "all 0.4s ease"
  },

  pulse: {
    transform: "scale(1.1)",
    boxShadow: "0 0 40px rgba(111,174,217,0.6)"
  },

  button: {
    padding: "12px 28px",
    borderRadius: 30,
    border: "none",
    background: "#2b6cb0",
    color: "white",
    cursor: "pointer",
    fontSize: 14,
    marginBottom: 40
  },

  report: {
    background: "white",
    padding: 30,
    borderRadius: 16,
    width: 420,
    boxShadow: "0 10px 30px rgba(0,0,0,0.08)"
  },

  heading: {
    fontWeight: 400,
    marginTop: 20
  },

  text: {
    fontWeight: 300,
    color: "#2d3748"
  }
};
