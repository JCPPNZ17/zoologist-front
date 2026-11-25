import streamlit as st

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

st.write(island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex)  # temporary check: remove once it works

"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""
