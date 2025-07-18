# 🛰️ Agentic Drone Reconnaissance Planner
![Static Badge](https://img.shields.io/badge/Python-3.8%2B-black)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![Static Badge](https://img.shields.io/badge/AgenticAI-LangChain-blue)


This project simulates a drone reconnaissance mission planner using **graph-based path planning**, **LangGraph for Agentic AI**, and **interactive mapping with Streamlit & Folium**. The app computes an optimal route between strategic AOIs (Areas of Interest) while intelligently avoiding threats such as SAM sites, radar stations, and no-fly zones.

> As I love working on graphs, maps, and now learning Agentic AI (LangGraph), I wanted to implement this project, which could be a great use case in the defense domain.

---

## 🚀 Features

- 🧠 **LangGraph Agent**: Used to simulate decision-making between multiple reasoning steps (AOI selection, threat analysis, and route optimization).
- 🗺️ **Folium Map**: Visualizes AOIs, threats, and the optimal route on an interactive map.
- 🔄 **Custom Threats**: Supports various military-style threats (e.g., Radar Stations, SAMs).
- 📍 **Drone Marker**: Visually marks the drone’s launch point or route start.
- ☁️ **Streamlit App**: Fully deployable to Streamlit Cloud with real-time path rendering.

---

## 📦 Tech Stack

| Tool         | Purpose                             |
|--------------|-------------------------------------|
| Python       | Core language                       |
| Streamlit    | Web app framework                   |
| Folium       | Interactive mapping (Leaflet)       |
| LangGraph    | Agentic reasoning engine            |
| NetworkX     | Graph-based route planning          |

---

## 🔧 Installation

```bash
git clone https://github.com/your-username/agentic-recon-planner.git
cd agentic-recon-planner
pip install -r requirements.txt
streamlit run app.py
```

## 🛰️ Use Case

This project mimics the decision workflow of a defense recon operation:

* Load AOIs and threats.
* Use an agent to validate feasibility and create a mission plan.
* uild a safe path avoiding threat zones.
* Visualize the route on an interactive map.

## Demo

Try it out here in the Streamlit Cloud : Link [here](https://portofaman-droneintelpath.streamlit.app/)

### Project is in progress

