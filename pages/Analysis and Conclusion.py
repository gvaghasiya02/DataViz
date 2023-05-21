import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="DataViz_Assignment-2",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "This is a DataViz Visualization Assignment 2 by **Gaurav Vaghasiya**"
    }
)
st.markdown('<a href="/" target="_self">Home</a>', unsafe_allow_html=True)

st.title("Analysis and Conslusion")
st.markdown("So as per analysis, most Unsegregated waste is contained in landfill bins, and people seem to confuse some sub-streams of recycling and compost thrown into the landfill bins. Almost 90% of Unsegregated waste is thrown into landfills and contains 60-70% of compost and others as recycled waste.")
st.markdown("Another analysis, some of the buildings have very good segregation percentages(over 50%) like Learning Commons, Malley, and Facilities while other buildings like Benson Center, and Swig has very less segregation percentage(under 20%) but yearly it is improving.")
st.markdown("I think more awareness is needed to spread and better categorization is needed as we see people seem to confuse the substream of waste categories. Let’s say paper, for example, various forms of paper can be in recycling(print papers), and compost(paper towels).With better Categorization, we can draw the line between all 3 categories and substreams. With this, we can improve segregation for better and more sustainable SCU.")
st.markdown('<h3 align="center">Thank You</h3>', unsafe_allow_html=True)
st.markdown('<br><br><p align="right"><a href="/Yearwise_Improvement" target="_self">Previous</a></p>', unsafe_allow_html=True)