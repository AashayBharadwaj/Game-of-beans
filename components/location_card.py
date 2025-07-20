# import streamlit as st
# import base64
# from data.data_dict_new import location_metrics
# from data.kpi_loader import get_kpi_metrics

# def load_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode('utf-8')

# def create_location_card(location_name, kpi_data):
#     meta = location_metrics[location_name]
#     kpi = kpi_data.get(location_name, {})

#     encoded_image = load_image(meta['Image'])

#     st.markdown(
#         f"""
#         <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:10px; padding:20px;
#                     margin:15px; text-align:left; box-shadow:4px 4px 15px rgba(0,0,0,0.1); width:230px;">
#             <img src="data:image/png;base64,{encoded_image}" style="width:100%; border-radius:10px; margin-bottom:10px;">
#             <h3 style="color:#0077b6; font-size:1.5rem; text-align:center; font-weight:bold;">{location_name}</h3>
#             <p style="color:#666; font-size:1rem; text-align:center;">Location Manager: {meta['Manager']}</p>
#             <hr style="border:none; height:1px; background-color:#ddd; margin:10px 0;">
#             <p><strong>Headcount:</strong> {kpi.get('Headcount', '--')}</p>
#             <p><strong>Turnover Rate:</strong> {kpi.get('Turnover Rate', '--')}</p>
#             <p><strong>Total Revenue:</strong> {kpi.get('Total Revenue', '--')}</p>
#             <p><strong>Planned Revenue:</strong> {meta['Planned Revenue']}</p>
#             <p><strong>Revenue per Employee:</strong> {kpi.get('Revenue per Employee', '--')}</p>
#             <button style="margin-top:10px; padding:5px 20px; background-color:#0077b6; color:white; border:none; border-radius:5px;">
#                 <a href="https://www.notion.so/Westeros-Org-Chart-22f43e065fed80beb499c7a339470e71?source=copy_link"
#                    style="text-decoration:none; color:white;">
#                    View Org Chart
#                 </a>
#             </button>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

import streamlit as st
import base64
from data.data_dict_new import location_metrics
from data.kpi_loader import get_kpi_metrics

def load_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def create_location_card(location_name, kpi_data):
    meta = location_metrics[location_name]
    kpi = kpi_data.get(location_name, {})

    encoded_image = load_image(meta['Image'])

    st.markdown(
        f"""
        <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:10px; padding:20px;
                    margin:15px; text-align:left; box-shadow:4px 4px 15px rgba(0,0,0,0.1);
                    width:230px; height:640px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
                <img src="data:image/png;base64,{encoded_image}" style="width:100%; border-radius:10px; margin-bottom:10px;">
                <h3 style="color:#0077b6; font-size:1.5rem; text-align:center; font-weight:bold;">{location_name}</h3>
                <p style="color:#666; font-size:1rem; text-align:center;">Location Manager: {meta['Manager']}</p>
                <hr style="border:none; height:1px; background-color:#ddd; margin:10px 0;">
                <p><strong>Avg Headcount:</strong> {kpi.get('Headcount', '--')}</p>
                <p><strong>Turnover Rate:</strong> {kpi.get('Turnover Rate', '--')}</p>
                <p><strong>Total Revenue:</strong> {kpi.get('Total Revenue', '--')}</p>
                <p><strong>Planned Revenue:</strong> {meta.get('Planned Revenue', '--')}</p>
                <p><strong>Revenue per Employee:</strong> {kpi.get('Revenue per Employee', '--')}</p>
            </div>
            <div style="text-align:center;">
                <a href="https://www.notion.so/Westeros-Org-Chart-22f43e065fed80beb499c7a339470e71?source=copy_link"
                   style="display:inline-block; margin-top:10px; padding:8px 16px; background-color:#0077b6;
                          color:white; border:none; border-radius:5px; text-decoration:none; font-weight:bold;">
                    View Org Chart
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
