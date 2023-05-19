import streamlit as st
import numpy as np
import pandas as pd
from plotly.graph_objs import Marker
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Interactive Visualisation")
st.markdown("The data contains a substantial amount of information regarding waste categorization at SCU over 8 years from 2015 to 2023. The theme of this interactive visualization is to demonstrate various types of waste generated, how improper placement of waste in different bins and buildings, as well as the improvements made over the years.")
st.markdown('<a href="/Types_of_Waste_Generated_at_SCU" target="_self">Types of Waste Generated at SCU</a>', unsafe_allow_html=True)
st.markdown('<a href="/Unsegregated_Waste_Classification" target="_self">Unsegregated Waste Classification</a>', unsafe_allow_html=True)
st.markdown('<a href="/Yearwise_Improvement" target="_self">Yearwise Improvement</a>', unsafe_allow_html=True)
st.markdown('<a href="/Analysis_and_Conclusion" target="_self">Analysis and Conclusion</a>', unsafe_allow_html=True)
st.markdown('<br><br><p align="right"><a href="/Types_of_Waste_Generated_at_SCU" target="_self">Next</a></p>', unsafe_allow_html=True)