import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "PSU1.png"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit for Geospatial Applications")

st.markdown(
    """
    This app is an interactive web app created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). 
    """
)

st.header("Instructions")

markdown = """
* For the [GitHub repository](https://github.com/opengeos/streamlit-map-template) or [use it as a template](https://github.com/opengeos/streamlit-map-template/generate) for your own project.
"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("Esri.NatGeoWorldMap")
m.to_streamlit(height=500)
