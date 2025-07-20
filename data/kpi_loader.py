import pandas as pd
from datetime import datetime

# File path to Excel
EXCEL_PATH = "data/Game_of_Beans_KPI_Data.xlsx"

def get_kpi_metrics(time_period="YTD"):
    df = pd.read_excel(EXCEL_PATH)
    df['Date'] = pd.to_datetime(df['Date'])

    today = datetime.today()
    current_year = today.year
    current_month = today.month

    if time_period == "YTD":
        df_filtered = df[df['Date'].dt.year == current_year]
    elif time_period == "MTD":
        df_filtered = df[(df['Date'].dt.year == current_year) & (df['Date'].dt.month == current_month)]
    elif time_period == "Last Year":
        df_filtered = df[df['Date'].dt.year == (current_year - 1)]
    else:
        df_filtered = df  # fallback to all

    # Group and aggregate
    summary = df_filtered.groupby("Location").agg({
        "Headcount": "mean",
        "Coffees Served": "sum",
        "Revenue": "sum",
        "Gross Profit": "sum",
        "Net Profit": "sum",
        "Client Satisfaction (%)": "mean",
        "Avg Ticket Size": "mean",
        "Loyalty Members": "max",
        "Events Hosted": "sum",
        "Training Hours": "sum",
        "Machine Downtime (hrs)": "sum"
    }).round(2).reset_index()

    # Turn into dictionary
    kpi_dict = {}
    for _, row in summary.iterrows():
        kpi_dict[row["Location"]] = {
            "Headcount": int(row["Headcount"]),
            "Turnover Rate": "—",  # Optional: derive later if needed
            "Total Revenue": f"₵{row['Revenue']:,.0f}",
            "Gross Profit": f"₵{row['Gross Profit']:,.0f}",
            "Net Profit": f"₵{row['Net Profit']:,.0f}",
            "Coffees Served": f"{int(row['Coffees Served']):,}",
            "Client Satisfaction": f"{row['Client Satisfaction (%)']:.1f}%",
            "Avg Ticket Size": f"₵{row['Avg Ticket Size']:.2f}",
            "Revenue per Employee": f"₵{(row['Revenue'] / row['Headcount']):,.0f}",
            "Loyalty Members": int(row["Loyalty Members"]),
            "Events Hosted": int(row["Events Hosted"]),
            "Training Hours": int(row["Training Hours"]),
            "Machine Downtime": f"{row['Machine Downtime (hrs)']} hrs"
        }

    return kpi_dict
