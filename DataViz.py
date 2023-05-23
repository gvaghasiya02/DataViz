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
st.title("Waste Analysis of SCU")
st.subheader("Interactive Visulization-Assignment-2")
st.caption("W1653448-Gaurav Vaghasiya")
st.markdown("The theme of this interactive visualization is to demonstrate various types of waste generated, how improper placement of waste in different bins and buildings, as well as the improvements made over the years.")
st.markdown('<a href="/Types_of_Waste_Generated_at_SCU" target="_blank">Types of Waste Generated at SCU</a>', unsafe_allow_html=True)
st.markdown('<a href="/Unsegregated_Waste_Classification" target="_blank">Unsegregated Waste Classification</a>', unsafe_allow_html=True)
st.markdown('<a href="/Yearwise_Improvement" target="_blank">Yearwise Improvement</a>', unsafe_allow_html=True)
st.markdown('<a href="/Analysis_and_Conclusion" target="_blank">Analysis and Conclusion</a>', unsafe_allow_html=True)
st.caption("*Operate through next/previous buttons to go through the story*")
st.markdown('<br><br><p align="right"><a href="/Types_of_Waste_Generated_at_SCU" target="_self">Next</a></p>', unsafe_allow_html=True)