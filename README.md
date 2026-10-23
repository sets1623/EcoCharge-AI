# EcoCharge AI
Smart, Solar-Aware EV Charging & Carbon-Saving System.

## Files
- `app.py`: Streamlit/Python source code.
- `EcoCharge_AI_Dashboard.html`: standalone browser dashboard that does not need Python packages.
- `requirements.txt`: dependencies for the Streamlit version.

## Open the browser dashboard
Double-click `EcoCharge_AI_Dashboard.html` in Microsoft Edge or Chrome. Change the inputs and click Update recommendation. You can download the comparison as CSV.

## Run the Streamlit version (if Python packages are allowed)
```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Limitations
This prototype performs transparent calculations from user-entered illustrative assumptions. It does not yet include a trained forecasting model, live data feeds, validated field measurements, or real charger control. The Windows machine used for development showed an Application Control policy block when importing pandas, so use the standalone HTML dashboard as the immediate demonstration path.
