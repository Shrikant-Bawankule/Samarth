import gradio as gr
import pandas as pd

# Load datasets
agri = pd.read_csv("RS_Session_258_AU_1212_2.csv")
rain = pd.read_csv("Sub_Division_IMD_2017.csv")

# Dropdown options
state_options = sorted(rain['SUBDIVISION'].dropna().unique().tolist())
year_options = sorted(rain['YEAR'].dropna().unique().astype(int).tolist())

# ---- Core Functions ----
def compare_rainfall(state1, state2, start_year, end_year):
    rain_filtered = rain[(rain['YEAR'] >= start_year) & (rain['YEAR'] <= end_year)]
    s1 = rain_filtered[rain_filtered['SUBDIVISION'].str.lower() == state1.lower()]
    s2 = rain_filtered[rain_filtered['SUBDIVISION'].str.lower() == state2.lower()]
    avg1 = s1['ANNUAL'].mean()
    avg2 = s2['ANNUAL'].mean()
    higher = (
        state1 if avg1 > avg2 else
        state2 if avg2 > avg1 else
        "Both have equal rainfall"
    )
    return {
        "State_1": state1,
        "Avg_Rainfall_1": round(avg1, 2) if pd.notna(avg1) else "N/A",
        "State_2": state2,
        "Avg_Rainfall_2": round(avg2, 2) if pd.notna(avg2) else "N/A",
        "Higher_Rainfall_State": higher
    }

def top_crops_by_production(top_n):
    column = "Quantity Procured - 2017-18"
    top_crops = agri[['Crop', column]].sort_values(by=column, ascending=False).head(top_n)
    result = [f"{i+1}. {row['Crop']} – {row[column]}" for i, row in top_crops.iterrows()]
    return "\n".join(result)

def rainfall_and_crop_summary(state1, state2, start_year, end_year, top_n):
    rain_result = compare_rainfall(state1, state2, start_year, end_year)
    crops = top_crops_by_production(top_n)
    return (
        f"🌧️ **Rainfall Comparison ({start_year}-{end_year})**\n\n"
        f"• {rain_result['State_1']}: {rain_result['Avg_Rainfall_1']} mm\n"
        f"• {rain_result['State_2']}: {rain_result['Avg_Rainfall_2']} mm\n"
        f"➡️ **Higher Rainfall:** {rain_result['Higher_Rainfall_State']}\n\n"
        f"🌾 **Top {top_n} Crops (Procurement 2017–18)**\n\n"
        f"{crops}\n\n"
        f"📘 **Sources:** data.gov.in (IMD & Ministry of Agriculture)"
    )

# ---- Clean Gradio Interface ----
with gr.Blocks(title="Project Samarth – Intelligent Agro-Climate Q&A System") as demo:
    gr.Markdown("### 🌾 Ask questions comparing rainfall and crop production using real data from data.gov.in")

    with gr.Row():
        state1 = gr.Dropdown(label="State 1", choices=state_options, allow_custom_value=True)
        state2 = gr.Dropdown(label="State 2", choices=state_options, allow_custom_value=True)

    with gr.Row():
        start_year = gr.Dropdown(label="Start Year", choices=year_options, value=2010, allow_custom_value=True)
        end_year = gr.Dropdown(label="End Year", choices=year_options, value=2017, allow_custom_value=True)

    with gr.Row():
        top_n = gr.Slider(label="Top N Crops", minimum=1, maximum=10, value=5, step=1)

    output = gr.Markdown(label="Answer")

    submit = gr.Button("Get Analysis")
    submit.click(
        rainfall_and_crop_summary,
        inputs=[state1, state2, start_year, end_year, top_n],
        outputs=output
    )

demo.launch(share = True)
