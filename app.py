import streamlit as st
import requests

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

"""
## Penguin characteristics
"""  # short section title rendered via Streamlit magic

island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])  # fixed options, so no typos reach the API
bill_length_mm = st.number_input("Bill length (mm)", min_value=0.0, value=51.9)  # float default -> returns a float
bill_depth_mm = st.number_input("Bill depth (mm)", min_value=0.0, value=19.5)  # same names as the API params
flipper_length_mm = st.number_input("Flipper length (mm)", min_value=0.0, value=206.0)  # min_value blocks negatives
body_mass_g = st.number_input("Body mass (g)", min_value=0.0, value=3950.0, step=50.0)  # step=50 makes +/- buttons useful for grams
sex = st.selectbox("Sex", ["Male", "Female"])  # capitalized exactly as the model expects

"""
## Prediction
"""  # section title via Streamlit magic

url = f"{st.secrets['API_URL']}/predict"  # base URL read from .streamlit/secrets.toml, endpoint added here

params = {  # keys must match the query parameters the API expects
    "island": island,
    "bill_length_mm": bill_length_mm,
    "bill_depth_mm": bill_depth_mm,
    "flipper_length_mm": flipper_length_mm,
    "body_mass_g": body_mass_g,
    "sex": sex,
}

if st.button("Predict"):  # True only on the rerun right after the click, so the API is called on demand
    response = requests.get(url, params=params)  # requests builds the ?key=value&... query string for us
    response.raise_for_status()  # stop with a clear error if the API returned 4xx/5xx

    result = response.json()  # dict returned by the API, e.g. {"prediction": "Chinstrap"}
    species = result["prediction"]  # extract just the species string using the key we saw

    st.success(f"🐧 Predicted species: **{species}**")  # shown only after clicking the button