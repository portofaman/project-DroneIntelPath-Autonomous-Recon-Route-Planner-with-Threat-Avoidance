import streamlit as st
from planner.map_graph import load_locations, render_map
from planner.agents import plan_route_with_agents

st.set_page_config(layout="wide")
st.title("🗺️ AgentRoute: Intelligent Itinerary Planner with Threat Awareness")

aois = load_locations("data/aoi.json")
threats = load_locations("data/threats.json")

aoi_names = [a['name'] for a in aois]
start = st.selectbox("Start Location", aoi_names)
end = st.selectbox("End Location", aoi_names, index=1)

if st.button("🧠 Plan Safe Route"):
    route, reasoning = plan_route_with_agents(aois, threats, start, end)
    st.success(f"✅ Route: {' ➜ '.join(route)}")

    st.markdown("### 🤖 AI Reasoning")
    for r in reasoning:
        st.markdown(f"- {r}")

    st.markdown("### 🗺️ Map View")
    route_map = render_map(aois, threats, route)
    st.components.v1.html(route_map._repr_html_(), height=500)
