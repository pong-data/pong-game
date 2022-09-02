import streamlit as st
import pandas as pd
import numpy as np

st.title('Analytics Pong Game')

df = pd.read_csv("../output/scores.csv")


# histogram of scores
st.subheader('distribution of scores')

# hist_values = np.histogram(df['Score'])
# hist_values = df['Score']
# hist_values = df['Score'].value_counts().rename_axis('unique_values').reset_index(name='count')
# hist_values = df['Score'].value_counts().rename_axis('unique_values')

# st.bar_chart(hist_values, bins = 10)
st.bar_chart(df, y='Score', x='Score')