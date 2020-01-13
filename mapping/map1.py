import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat_list=list(data["LAT"])
lon_list=list(data["LON"])
elev_list=list(data["ELEV"])

def color_producer(elev):
    result = ""
    if elev<=1000:
        result="green"
    elif 1000<elev<=3000:
        result="orange"
    else:
        result="red"

    return result

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fgv=folium.FeatureGroup(name="Volcanoes")
for coordinate1,coordinate2,elevation in zip(lat_list,lon_list,elev_list):
    fgv.add_child(folium.CircleMarker(location=[coordinate1,coordinate2],radius=6,popup=str(elevation)+"m",fill_color=color_producer(elevation),color="grey",fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor":"green" if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))
#if x["properties"]["POP2005"]<10000000
#else 'orange' if 10000000<=x["properties"]["POP2005"]<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Maphome.html")
