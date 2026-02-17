"use client";

import { useState } from "react";

export default function Home() {
    const [loading, setLoading] = useState(false);
    const [report, setReport] = useState<any>(null);

    const runSwarm = async () => {
        try {
            setLoading(true);

            const res = await fetch(
                "https://swarm-cardio-os.onrender.com/analyze"
            );

            if (!res.ok) throw new Error("API Failure");

            const data = await res.json();
            setReport(data);

        } catch (err) {
            console.error("Swarm Error:", err);
            alert("Swarm Engine Connection Failed");
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="container">
            <h1 className="title">
                CardioSphere Intelligence
            </h1>

            <div className={`sphere ${loading ? "pulse" : ""}`} />

            <button className="runButton" onClick={runSwarm}>
                {loading ? "Analyzing…" : "Run Swarm Engine"}
            </button>

            {report && (
                <div className="report">
                    <section>
                        <h2>Decision Overview</h2>
                        <p>{report.Decision}</p>
                    </section>

                    <section>
                        <h2>Risk Probability</h2>
                        <p>{report.RiskProbability}</p>
                    </section>

                    <section>
                        <h2>Composite Score</h2>
                        <p>{report.CompositeScore}</p>
                    </section>
                </div>
            )}
        </main>
    );
}
