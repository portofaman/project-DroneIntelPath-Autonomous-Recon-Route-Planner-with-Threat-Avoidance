import json
import folium

def load_locations(path):
    with open(path, "r") as f:
        return json.load(f)

def render_map(aois, threats, route):
    m = folium.Map(location=[aois[0]["lat"], aois[0]["lon"]], zoom_start=6)

    for aoi in aois:
        color = "green" if aoi["name"] in route else "blue"
        folium.Marker([aoi["lat"], aoi["lon"]], popup=aoi["name"], icon=folium.Icon(color=color)).add_to(m)

    for t in threats:
        folium.Circle(
            radius=50000,
            location=[t["lat"], t["lon"]],
            color="red",
            fill=True,
            fill_opacity=0.3,
            popup=t["name"],
            tooltip=t["name"]
        ).add_to(m)

    for i in range(len(route) - 1):
        latlon1 = next((a for a in aois if a["name"] == route[i]), None)
        latlon2 = next((a for a in aois if a["name"] == route[i+1]), None)
        if latlon1 and latlon2:
            folium.PolyLine(
                locations=[[latlon1["lat"], latlon1["lon"]], [latlon2["lat"], latlon2["lon"]]],
                color="black"
            ).add_to(m)

    return m
