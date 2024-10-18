import streamlit as st
from afm_analysis.data_loader import load_heights, load_force_data
from afm_analysis.slope_estimator import estimate_slope
from afm_analysis.visualizer import plot_force_distance_curve, generate_heatmap

# Streamlit interface
st.title("AFM Data Analysis")

# File uploader for heights data
heights_file = st.file_uploader("Upload AFM heights data (.npy)", type=["npy"])
if heights_file is not None:
    heights = load_heights(heights_file)
    st.write("Heights data loaded successfully!")
    generate_heatmap(heights)

# File uploader for force-distance data
force_file = st.file_uploader("Upload AFM force data (Pickle)", type=["pkl"])
if force_file is not None:
    force_data = load_force_data(force_file)
    curve = force_data.get("curve")
    st.write("Force-distance data loaded successfully!")

    # Slope estimation
    slope = estimate_slope(curve, force_data['s'])
    st.write(f"Estimated slope: {slope}")
    plot_force_distance_curve(curve, slope)
