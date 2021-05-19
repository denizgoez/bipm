import streamlit as st 
import requests
import json
import time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import mpl_toolkits
import pandas as pd

st.title("Names and Number of People on ISS")

st.markdown("""
This app uses API to get the names of people on the ISS as well as display them.
It also tracks the location of the iss, refreshing every 5 seconds
""")


def get_location(geo=True):
    iss_loc = requests.get("http://api.open-notify.org/iss-now.json")
    loc = json.loads(iss_loc.text)
    lon = float(loc["iss_position"]["longitude"])
    lat = float(loc["iss_position"]["latitude"])
    timestamp = loc["timestamp"]
    datetime = time.strftime("%A, %Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    return lon, lat, datetime

lon, lat, datetime = get_location()
a = pd.DataFrame([[lat, lon]], columns=["lat","lon"])
st.map(a)s