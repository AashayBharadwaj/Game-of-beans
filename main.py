import streamlit as st
import plotly.express as px

from components.layout import render_header
from components.sidebar import select_time_period_and_metric
from components.location_card import create_location_card
from data.data_dict_new import location_metrics
from data.kpi_loader import get_kpi_metrics

st.set_page_config(initial_sidebar_state="collapsed")

def main():
    # --- HEADER ---
    render_header()

    # --- SIDEBAR FILTERS ---
    time_period, selected_metric = select_time_period_and_metric()

    # --- KPI DATA ---
    kpi_data = get_kpi_metrics(time_period)
    locations = list(location_metrics.keys())

    # --- CONSOLIDATED KPI CHART DATA PREP ---
    metric_values = []
    valid_locations = []

    for loc in locations:
        kpi = kpi_data.get(loc, {})
        value = kpi.get(selected_metric, None)

        if isinstance(value, str):
            value = value.replace("₵", "").replace(",", "").strip()

        try:
            metric_values.append(float(value))
            valid_locations.append(loc)
        except:
            continue

    # --- PLOTLY BAR CHART ---
    if metric_values:
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 20px;">
                <h3 style="font-size: 1.6rem; margin-bottom: 0.3rem;">⚔️ Consolidated Metric View ⚔️</h3>
                <div style="font-size: 1rem;">Showing <strong>{time_period}</strong> data!</div>
                <div style="font-size: 0.9rem; margin-top: 0.3rem;">Use the dropdowns in the sidebar to explore different metrics and time periods.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        chart_df = {
            "Location": valid_locations,
            selected_metric: metric_values
        }

        custom_colors = [
            "#c08457", "#b5a27e", "#a5b4ac", "#d8b4a0", "#a3a380",
            "#e2c290", "#af8260", "#c9ada1", "#b7b597"
        ]

        fig = px.bar(
            chart_df,
            x="Location",
            y=selected_metric,
            color="Location",
            text_auto=".2s",
            color_discrete_sequence=custom_colors
        )

        fig.update_layout(
            xaxis_tickangle=-45,
            showlegend=False,
            plot_bgcolor="#ffffff",
            xaxis_showgrid=False,
            yaxis_showgrid=False,
            xaxis_title=None,
            yaxis_title=selected_metric,
            margin=dict(t=20),
            xaxis_showline=False,
            yaxis_showline=False,
            yaxis_type = "log"
            
        )

        st.plotly_chart(fig, use_container_width=True)

        # Chart title below chart
        st.markdown(
            f"<div style='text-align:center; font-weight:500; font-size:1.1rem; margin-top:0.5rem;'>{selected_metric} by Location</div>",
            unsafe_allow_html=True
        )

    else:
        st.info(f"No valid data available for metric: {selected_metric}")

    # --- TRANSITION TEXT BETWEEN CHART AND CARDS ---
    st.markdown("""
    <hr style="margin: 2rem 0; border: none; border-top: 1px solid #ddd;">
    <h4 style="text-align: center; font-size: 1.3rem; margin-bottom: 0.5rem;">📍 Location-wise Details</h4>
    <p style="text-align: center; font-size: 1rem;">
        A breakdown of key performance indicators for each coffee shop location. Use this view to explore how each team is performing individually.
    </p>
    """, unsafe_allow_html=True)

    # --- KPI CARDS BELOW ---
    for i in range(0, len(locations), 3):
        cols = st.columns(3)
        for idx, col in enumerate(cols):
            if i + idx < len(locations):
                with col:
                    create_location_card(locations[i + idx], kpi_data)

if __name__ == "__main__":
    main()
