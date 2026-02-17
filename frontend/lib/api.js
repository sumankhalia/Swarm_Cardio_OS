export async function runSwarm() {

    const res = await fetch(
        "https://swarm-cardio-os.onrender.com/analyze"
    );

    return res.json();
}
