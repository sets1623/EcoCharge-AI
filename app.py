"""
EcoCharge AI — Smart, Solar-Aware EV Charging & Carbon-Saving System
Educational prototype. Uses illustrative user inputs; not connected to a real charger.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoCharge AI", page_icon="⚡", layout="wide")
st.title("⚡ EcoCharge AI")
st.subheader("Smart, Solar-Aware EV Charging & Carbon-Saving System")
st.caption("Educational decision-support prototype using illustrative inputs.")

with st.sidebar:
    st.header("EV Charging Inputs")
    energy_kwh = st.number_input("Energy needed (kWh)", min_value=1.0, max_value=100.0, value=20.0, step=1.0)
    immediate_tariff = st.number_input("Immediate tariff (₹/kWh)", min_value=1.0, max_value=50.0, value=8.0, step=0.5)
    recommended_tariff = st.number_input("Recommended-slot tariff (₹/kWh)", min_value=1.0, max_value=50.0, value=6.0, step=0.5)
    grid_factor = st.number_input("Grid emissions (kg CO₂/kWh)", min_value=0.0, max_value=2.0, value=0.70, step=0.05)
    solar_share_percent = st.slider("Estimated solar share (%)", 0, 100, 60)

solar_share = solar_share_percent / 100.0

# Transparent baseline calculations
immediate_cost = energy_kwh * immediate_tariff
recommended_cost = energy_kwh * recommended_tariff
immediate_emissions = energy_kwh * grid_factor
recommended_emissions = energy_kwh * (1.0 - solar_share) * grid_factor

st.info("Illustrative prototype only. Replace assumptions with measured/local data before reporting real-world impact.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Immediate cost", f"₹{immediate_cost:.2f}")
c2.metric("Recommended cost", f"₹{recommended_cost:.2f}", f"₹{immediate_cost - recommended_cost:.2f} difference")
c3.metric("Immediate emissions", f"{immediate_emissions:.2f} kg CO₂")
c4.metric("Recommended emissions", f"{recommended_emissions:.2f} kg CO₂",
          f"{immediate_emissions - recommended_emissions:.2f} kg estimated difference")

comparison = pd.DataFrame({
    "Strategy": ["Charge immediately", "Solar-aware recommended slot"],
    "Estimated cost (₹)": [immediate_cost, recommended_cost],
    "Estimated emissions (kg CO₂)": [immediate_emissions, recommended_emissions],
    "Solar share (%)": [0, solar_share_percent],
})

st.header("Charging Strategy Comparison")
st.dataframe(comparison, use_container_width=True, hide_index=True)

left, right = st.columns(2)
with left:
    fig, ax = plt.subplots()
    ax.bar(comparison["Strategy"], comparison["Estimated cost (₹)"])
    ax.set_title("Estimated Charging Cost")
    ax.set_ylabel("Cost (₹)")
    ax.tick_params(axis="x", rotation=10)
    st.pyplot(fig)
    plt.close(fig)

with right:
    fig, ax = plt.subplots()
    ax.bar(comparison["Strategy"], comparison["Estimated emissions (kg CO₂)"])
    ax.set_title("Estimated Carbon Emissions")
    ax.set_ylabel("kg CO₂")
    ax.tick_params(axis="x", rotation=10)
    st.pyplot(fig)
    plt.close(fig)

st.header("Recommendation")
if recommended_cost <= immediate_cost and recommended_emissions <= immediate_emissions:
    st.success(
        f"Under these assumptions, the recommended slot costs ₹{immediate_cost - recommended_cost:.2f} less "
        f"and has {immediate_emissions - recommended_emissions:.2f} kg lower estimated grid emissions."
    )
else:
    st.warning("Compare the cost and emissions trade-offs. The recommended slot is not better on both measures.")

st.download_button(
    "Download comparison CSV",
    comparison.to_csv(index=False).encode("utf-8"),
    file_name="ecocharge_comparison.csv",
    mime="text/csv",
)

st.caption(
    "Simplified method: cost = energy × tariff; immediate emissions = energy × grid factor; "
    "recommended emissions = energy × (1 − solar share) × grid factor. "
    "Assumes solar share offsets grid electricity proportionally."
)
