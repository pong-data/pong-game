
import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit.elements import image

# Parameters
path_output_scores = "../output/scores.csv"

# Set title of web app
st.set_page_config(
    page_title="Pong!",
    page_icon='img/favicon.png',
    layout="wide",
)

st.markdown('<style>body{background-color: Magenta;}</style>', unsafe_allow_html=True)

title_container = st.container()
c1, c2 = st.columns([10, 90])
with title_container:
    with c1:
        st.image('../img/favicon.png', width=64)
    with c2:
        st.markdown('<h1 style="color: purple; vertical-align: baseline;">Pong Game Analytics</h1>',
                    unsafe_allow_html=True)

def get_data() -> pd.DataFrame:
    return pd.read_csv(path_output_scores)

placeholder = st.empty()

for seconds in range(10*60*60):
    # Read csv with output scores
    df = get_data()

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Number of players",
            value=df.shape[0],
        )

        # kpi2.metric(
        #     label="Married Count 💍",
        #     value=int(count_married),
        #     delta=-10 + count_married,
        # )
        #
        # kpi3.metric(
        #     label="A/C Balance ＄",
        #     value=f"$ {round(balance, 2)} ",
        #     delta=-round(balance / count_married) * 100,
        # )

        # Set dashboard title
        # st.markdown(
        #     title_container
        # )

        # Create two columns
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Highscore")
            fig1 = st.table(df.loc[:, ['Naam', 'Score']].sort_values(by='Score', ascending=False).iloc[0:10, :])
            # st.write(fig1)

        with col2:
            st.markdown("### Distribution of scores")
            fig2 = px.histogram(data_frame=df, x="Score", nbins=20)
            st.write(fig2)

        # hist_values = np.histogram(df['Score'])
        # hist_values = df['Score']
        # hist_values = df['Score'].value_counts().rename_axis('unique_values').reset_index(name='count')
        # hist_values = df['Score'].value_counts().rename_axis('unique_values')

        # st.bar_chart(hist_values, bins = 10)
        # st.bar_chart(df, y='Score', x='Score')

        time.sleep(3)


