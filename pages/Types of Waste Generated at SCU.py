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

df = pd.read_csv('assign2_wastedata.csv')
def split_stream(stream: str):
    resp = stream.split(" in ")
    if len(resp) == 1:
      return resp[0].strip(), resp[0].strip(), str("Segregated")
    else:
      if resp[0].strip()=="Food Waste" and resp[1].strip()=="Compost":
        return resp[1].strip(), resp[1].strip(), str("Segregated")
      elif resp[0].strip()=="Reusables" and resp[1].strip()=="Landfill":
        return resp[1].strip(), resp[1].strip(), str("Segregated")
      else:
        if resp[0].strip()=="Food Waste":
            return str("Compost"), resp[1].strip(), str("Unsegregated")
        elif resp[0].strip()=="Reusables":
            return str("Landfill"), resp[1].strip(), str("Unsegregated")
        else:
            return resp[0].strip(), resp[1].strip(), str("Unsegregated")

Finaldf = df.join(pd.DataFrame(df['Stream'].apply(split_stream).tolist(), columns=["Waste Type", "Disposed In", "Status"]))
Finaldf['Date'] = pd.to_datetime(Finaldf['Date'], format='%m/%d/%y')

Finaldf['Year'] = Finaldf['Date'].dt.year

st.header("Types of Waste Generated at SCU")

st.subheader("Idea:")
st.markdown("The idea behind this visualization is to show what type of waste is generated over 8 years at SCU with the bubble chart.")
st.subheader("Visual Features:")
st.markdown("Each bubble represents the substream of the waste on the x-axis it represents the volume of the waste, and the y-axis represents what was the bin of the waste. The color of the bubble represents the type of waste whereas recycling represents blue, green for compost, and grey for landfill. Each bubble size represents the weight of the waste. As an interactive element, hovering over each bubble will give details of the substream and values of weight, volume, type of waste, and where it was thrown. Also, the radio button changes the classification, based on segregated and unsegregated.")

option = st.radio("Select the attribute",('Segregated', 'Unsegregated'))

Finaldf=Finaldf.loc[Finaldf['Status']==option]
waste=Finaldf.groupby(['Building','Disposed In','Waste Type','Substream']).agg({'Weight':'sum', 'Volume':'sum'}).reset_index()

fig = px.scatter(waste, x="Volume", y="Disposed In",
	         size='Weight', color="Waste Type", hover_name="Substream", color_discrete_map={'Landfill':'grey','Recycling':'blue', 'Compost':'green'}, size_max=60)
st.plotly_chart(fig,use_container_width=True, theme="streamlit")
st.caption("*Operate through next/previous buttons to go through the story*")
st.markdown('<br><br><p align="right"><a href="/" target="_self">Previous</a>&nbsp;|&nbsp;<a href="/Unsegregated_Waste_Classification" target="_self">Next</a></p>', unsafe_allow_html=True)