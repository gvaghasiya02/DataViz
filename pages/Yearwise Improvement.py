import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

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

st.header("Yearwise Improvement")

st.subheader("Idea:")
st.markdown("The idea behind this bar graph is to represent the improvement over the years by each building in the segregation of waste.")
st.subheader("Visual Features:")
st.markdown("Radio button to analyze based on volume and weight, On the x-axis we have a time frame, and on the y-axis weight/volume. Each bar will represent segregated(green) and unsegregated(red) waste with color. Also, with animation frame will have the building as an attribute. So, we can see an improvement in segregation for each building.")

option = st.radio("Select the attribute",('Weight', 'Volume'))

im=Finaldf.groupby(['Year','Building','Status']).agg({option:'sum'}).reset_index()
pr = (Finaldf.groupby(['Year','Building','Status']).agg({option:'sum'})*100/Finaldf.groupby(['Year','Building']).agg({option:'sum'})).reset_index()
fig=px.bar(
             im, x="Year", y=option, color="Status", color_discrete_map={'Segregated':'green','Unsegregated':'red'}, text=pr[option].apply(lambda x: '{0:1.2f}%'.format(x)), animation_frame='Building', range_x=[2014,2023], height=800, width=1000)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000
st.plotly_chart(fig,use_container_width=True, theme="streamlit")
st.markdown('<br><br><p align="right"><a href="/Unsegregated_Waste_Classification" target="_self">Previous</a>&nbsp;|&nbsp;<a href="/Analysis_and_Conclusion" target="_self">Next</a></p>', unsafe_allow_html=True)