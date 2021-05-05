# Import Package
import streamlit as st
import pandas as pd
import pylab
import altair as alt
import matplotlib.pyplot as plt
from matplotlib import pyplot

# Import data
# df = pd.read_csv("C:/Users/deniz/OneDrive - HWR Berlin/2. sem/Big Data and Architectures/gapminderviz-master/gapminder_tidy.csv")
# Import data
df = pd.read_csv(r'C:\\Users\deniz\OneDrive - HWR Berlin\2. sem\Big Data and Architectures\gapminder_tidy.csv')
df1=df.drop(columns=['fertility', 'child_mortality', 'region'], axis=1)

# Draw a title and some text to the app:
'''
# Streamlit App

Data from gapminder
'''

@st.cache
def get_data():
    return pd.read_csv('https://datahub.io/core/gdp/r/gdp.csv')

'# World GDP'

df = get_data()

min_year = int(df['Year'].min())
max_year = int(df['Year'].max())

countries = df1['Country'].unique()

'## By year'
year = st.slider('Year', min_year, max_year)
df1[df1['Year'] == year]

'## By country'
country = st.selectbox('Country', countries)
df1[df1['Country'] == country]


with st.echo(code_location='below'):
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(
        df1["gdp"],
        df1["life"],
    )

    ax.set_xlabel("GDP")
    ax.set_xscale('log')
    ax.set_ylabel("Life expectancy")

    st.write(fig)
