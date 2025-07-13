import streamlit as st
import pandas as pd
import base64
from data.data_dict_new import location_metrics

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Game of Beans",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------
# Load and Encode Banner Image
# -------------------------
def load_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

banner_base64 = load_image_base64("assets/cover_light.png")

# -------------------------
# ☕ Banner Display
# -------------------------
st.markdown(
    f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="data:image/png;base64,{banner_base64}" 
             style="width: 100%; max-height: 80vh; object-fit: cover;" />
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------
# 🎯 Title + Subtitle
# -------------------------
st.markdown(
    "<h1 style='text-align: center;'>Game of Beans</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style="text-align: center; font-weight: normal; color: gray;">
        From the Night's Watch to Dorne, monitor how our 15 legendary outlets are brewing success.<br>
        Use the sidebar to navigate through the map view, outlet scorecards, and detailed insights.
    </h4>
    """,
    unsafe_allow_html=True
)

# -------------------------
# 📊 Metrics Section
# -------------------------
df = pd.read_csv("data/outlets.csv", encoding="ISO-8859-1")
df.columns = df.columns.str.strip()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Outlets", len(df))

with col2:
    st.metric("Total Weekly Revenue", f"${df['weekly_sales'].sum():,.0f}")

with col3:
    st.metric("Total Coffees Served", f"{df['coffees_served'].sum():,}")

st.info("🔍 Use the sidebar to start exploring outlet performance.")

# -------------------------
# 🏰 Outlet Summary Cards
# -------------------------
def load_placeholder_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

placeholder_img = load_placeholder_base64("assets/cover.png")

st.markdown("### 🏰 Outlet Summary Cards")
locations = list(location_metrics.keys())

for i in range(0, len(locations), 3):
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        if i + idx < len(locations):
            loc = locations[i + idx]
            data = location_metrics[loc]
            with col:
                st.markdown(f"""
                <div style="
                    background-color: #fff;
                    border: 1px solid #ddd;
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 15px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
                    text-align: center;
                    ">
                    <img src="data:image/png;base64,{placeholder_img}" style="width: 100%; border-radius: 10px; height: 150px; object-fit: cover; margin-bottom: 10px;">
                    <h3 style="color: #0077b6; margin-bottom: 5px;">{loc}</h3>
                    <p style="margin: 0; color: #444;"><strong>Manager:</strong> {data['Manager']}</p>
                    <p style="margin: 0;"><strong>Revenue:</strong> {data['Total Revenue']}</p>
                    <p style="margin: 0;"><strong>Headcount:</strong> {data['Headcount']}</p>
                </div>
                """, unsafe_allow_html=True)
