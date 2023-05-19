import streamlit as st
import numpy as np
import pandas as pd
from plotly.graph_objs import Marker
import plotly.express as px
import matplotlib.pyplot as plt

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

Finaldf=Finaldf.loc[Finaldf['Status']=="Unsegregated"]

st.header("Unsegregated Waste Classification")

st.subheader("Idea:")
st.markdown("This sunburst will specifically focus on unsegregated waste classification. This will represent how wrongly waste is classified and what is the percentage of specific waste in a particular category.")
st.subheader("Visual Features:")
st.markdown("Provided radio button which will select attribute between weight and volume on which classification is done. The sunburst chart will represent the building on the first level then the disposed bin, waste type, and after that substream of waste. Each level will have a percentage from parents to get analysis and hovering over each part will give information to other levels. As an interactive chart, each section can be zoomed out and get a better idea of its children’s value. Can be abstracted on various levels we can analyze data for buildings and how each building is doing each type of waste category. Also coloring of sections is based on category whereas recycling represents blue, green for compost, and grey for landfill.")

option = st.radio("Select the attribute",('Weight', 'Volume'))

building_weight=Finaldf.groupby(['Building','Disposed In','Status','Waste Type','Date', 'Substream']).agg({option:'sum'}).reset_index()

fig=px.sunburst(
    building_weight,
    path=['Building','Disposed In','Waste Type','Substream'],
    values=option, height=1000, width=1000, title="Based on "+option, color='Waste Type', color_discrete_map={'(?)':['yellow','red','orange','pink','purple'],'Landfill':'grey','Recycling':'blue', 'Compost':'green'})
fig.update_traces(textinfo="label+percent parent+value")
st.plotly_chart(fig,use_container_width=True, theme="streamlit")
st.markdown('<br><br><p align="right"><a href="/Types_of_Waste_Generated_at_SCU" target="_self">Previous</a>&nbsp;|&nbsp;<a href="/Yearwise_Improvement" target="_self">Next</a></p>', unsafe_allow_html=True)