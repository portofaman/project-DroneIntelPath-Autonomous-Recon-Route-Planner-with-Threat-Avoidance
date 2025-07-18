import networkx as nx
from langgraph.graph import StateGraph, END
from typing import TypedDict, List


class PlannerState(TypedDict):
    aois: list
    threats: list
    graph: nx.Graph
    start: str
    end: str
    route: List[str]
    reasoning: List[str]

def point_to_segment_distance(px, py, x1, y1, x2, y2):
    """Returns the shortest distance between point (px, py) and line segment (x1, y1)-(x2, y2)"""
    from numpy import array, dot, clip, linalg
    p, a, b = array([px, py]), array([x1, y1]), array([x2, y2])
    d = b - a
    t = clip(dot(p - a, d) / dot(d, d), 0, 1)
    projection = a + t * d
    return linalg.norm(p - projection)

def build_graph_node(state: PlannerState) -> PlannerState:
    aois, threats = state["aois"], state["threats"]
    G = nx.Graph()

    for a in aois:
        G.add_node(a['name'], pos=(a['lat'], a['lon']))

    for i, a1 in enumerate(aois):
        for j, a2 in enumerate(aois):
            if i != j:
                dist = ((a1['lat'] - a2['lat'])**2 + (a1['lon'] - a2['lon'])**2) ** 0.5
                threat_penalty = 0

                for threat in threats:
                    threat_dist = point_to_segment_distance(
                        threat["lat"], threat["lon"],
                        a1["lat"], a1["lon"],
                        a2["lat"], a2["lon"]
                    )
                    if threat_dist < 0.5:  # Adjust sensitivity
                        threat_penalty += 100  # Heavy penalty for crossing near threat

                G.add_edge(a1['name'], a2['name'], weight=dist + threat_penalty)

    state['graph'] = G
    state['reasoning'] = ["Graph built with edge-level threat penalty."]
    return state



def route_planner_node(state: PlannerState) -> PlannerState:
    G = state['graph']
    path = nx.shortest_path(G, source=state['start'], target=state['end'], weight='weight')
    state['route'] = path
    state['reasoning'].append(f"Planned route: {' ➜ '.join(path)}")
    return state


def plan_route_with_agents(aois, threats, start, end):
    state = PlannerState(aois=aois, threats=threats, start=start, end=end, graph=None, route=[], reasoning=[])

    graph = StateGraph(PlannerState)
    graph.add_node("build_graph", build_graph_node)
    graph.add_node("plan_route", route_planner_node)

    graph.set_entry_point("build_graph")
    graph.add_edge("build_graph", "plan_route")
    graph.set_finish_point("plan_route")

    app = graph.compile()
    final_state = app.invoke(state)
    return final_state["route"], final_state["reasoning"]
