import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Marker clusters represent information composed of Virginia 
State Police investigators and local law enforcement used 
for soliciting tips on unsolved cases throughout the 
Commonwealth on the Virginia Cold Case Database
Source: (https://coldcase.vsp.virginia.gov/) - Date: 09/06/2024
****The page was created from a Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Virginia Cold Case Public Database 1961 to 2023")

       m = leafmap.Map(center=[37.55162945255474, -76.68277538321168], zoom=8, google_map="HYBRID")
        cases = "cleaned_ccdb_st2.csv"
                
        m.add_points_from_xy(
            cases,
            x="Lon",
            y="Lat",
            color_column="type",
            spin=True,
            add_legend=True,            
        )

m.to_streamlit(height=700)
