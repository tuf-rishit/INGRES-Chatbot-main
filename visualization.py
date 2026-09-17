import streamlit as st
import pandas as pd
import altair as alt

def show_chart(df):
    """
    Expects a DataFrame with at least:
    - Year
    - EXTRACTED_GW_MCM
    - TOTAL_EXTRACTABLE_GW_MCM
    """

    df = df.sort_values(by="Year")

    st.write("### 📈 Groundwater Extraction Trend")

    chart1 = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x=alt.X("Year:Q", axis=alt.Axis(title="Year", format="d")),
            y=alt.Y("EXTRACTED_GW_MCM:Q", axis=alt.Axis(title="Extracted Groundwater (MCM)")),
            tooltip=["Year", "EXTRACTED_GW_MCM"]
        )
        .properties(height=300)
    )

    st.altair_chart(chart1, use_container_width=True)

    st.write("### 💧 Total Extractable Groundwater")

    chart2 = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x=alt.X("Year:Q", axis=alt.Axis(title="Year", format="d")),
            y=alt.Y("TOTAL_EXTRACTABLE_GW_MCM:Q", axis=alt.Axis(title="Total Extractable Groundwater (MCM)")),
            tooltip=["Year", "TOTAL_EXTRACTABLE_GW_MCM"]
        )
        .properties(height=300)
    )

    st.altair_chart(chart2, use_container_width=True)

def show_map():
    st.write("🌍 Map visualization will appear here (GIS integration placeholder)")