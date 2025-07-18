import streamlit as st
import base64
from data.data_dict_new import location_metrics  # Import the updated dummy data with images

st.set_page_config(initial_sidebar_state="collapsed")

def load_image(image_path):
    """Helper function to encode an image file to base64."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def create_location_card(location_name):
    """Function to create a card with metrics, an image, manager info, and a button to view the org chart for a location."""
    metrics = location_metrics[location_name]  # Fetch metrics for the location
    encoded_image = load_image(metrics['Image'])

    st.markdown(
        f"""
        <div style="
            background-color: #ffffff; 
            border: 1px solid #ddd; 
            border-radius: 10px; 
            padding: 20px; 
            margin: 15px;  
            text-align: left; 
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
            width: 230px; 
            height: auto; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;">
            <img src="data:image/png;base64,{encoded_image}" style="width: 100%; border-radius: 10px; margin-bottom: 10px;">
            <h3 style="color: #0077b6; font-size: 1.5rem; margin: 0; text-align: center; font-weight: bold;">
                {location_name}
            </h3>
            <p style="color: #666; font-size: 1rem; margin-top: 5px; text-align: center;">
                Location Manager: {metrics['Manager']}
            </p>
            <hr style="border: none; height: 1px; background-color: #ddd; margin: 10px 0;">
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Headcount:</strong> {metrics['Headcount']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Turnover Rate:</strong> {metrics['Turnover Rate']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Total Revenue:</strong> {metrics['Total Revenue']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Planned Revenue:</strong> {metrics['Planned Revenue']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Revenue per Employee:</strong> {metrics['Revenue per Employee']}</p>
            <button style="margin-top: 10px; padding: 5px 20px; font-size: 0.9rem; background-color: #0077b6; color: white; border: none; border-radius: 5px;">
                    <a href="https://www.notion.so/Westeros-Org-Chart-22f43e065fed80beb499c7a339470e71?source=copy_link" style="text-decoration: none; color: white;" onclick="document.getElementById('org-chart-image').style.display='block';return false;">
                        View Org Chart
                    </a>
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )

    



def main():

    st.image(
        "assets/cover_light.png",  # Replace with the path to your image
        use_container_width=True  # Ensures the image spans the full width
    )

    st.markdown(
        "<h1 style='text-align: center;'>Westeros Coffee Shop Performance Overview</h2>",
        unsafe_allow_html=True,
    )

    # st.markdown(
    #     """
    #     <h2 style="font-size: 2 rem; font-weight: bold; margin-bottom: 10px; text-align: center;">
    #     KNOW YOUR NUMBERS!<br>LEAD THE GAME!!
    #     </h1>
    #     """,
    #     unsafe_allow_html=True
    # )


    # Add a dropdown to select the time period
    st.sidebar.title('Select a time period')
    time_period = st.sidebar.selectbox(
        "Select Time Period:",
        ["YTD", "MTD", "Last Year"],
        index=0  # Default to "YTD"
    )

    # Display selected time period
    st.markdown(
        f"""
        <div style="text-align: center; font-size: 1rem; margin-top: 10px;">
            Showing <strong>{time_period}</strong> data!
        </div>
        """,
        unsafe_allow_html=True
    )

    # Get all location names
    locations = list(location_metrics.keys())

    # Display cards
    for i in range(0, len(locations), 3):
        cols = st.columns(3)
        for idx, col in enumerate(cols):
            if i + idx < len(locations):
                with col:
                    create_location_card(locations[i + idx])

if __name__ == "__main__":
    main()