import os
from dotenv import load_dotenv
import streamlit as st
import requests
from streamlit_extras.let_it_rain import rain

# load environment variables from .env file
load_dotenv()

# Get the BASE_URL from the environment variables
base_url = os.getenv("BASE_URL", "http://localhost:8000")


# Streamlit app title and description
st.title("Breast Cancer Prediction")
st.write("Enter the values for each feature to predict if the tumor is benign or malignant.")

# Input fields
clump_thickness = st.number_input("Clump Thickness", min_value=1, max_value=10, value=1)
uniformity_of_cell_size = st.number_input("Uniformity of Cell Size", min_value=1, max_value=10, value=1)
uniformity_of_cell_shape = st.number_input("Uniformity of Cell Shape", min_value=1, max_value=10, value=1)
marginal_adhesion = st.number_input("Marginal Adhesion", min_value=1, max_value=10, value=1)
single_epithelial_cell_size = st.number_input("Single Epithelial Cell Size", min_value=1, max_value=10, value=1)
bare_nuclei = st.number_input("Bare Nuclei", min_value=1, max_value=10, value=1)
bland_chromatin = st.number_input("Bland Chromatin", min_value=1, max_value=10, value=1)
normal_nucleoli = st.number_input("Normal Nucleoli", min_value=1, max_value=10, value=1)
mitoses = st.number_input("Mitoses", min_value=1, max_value=10, value=1)

# Prediction button
if st.button("Predict"):
    # Prepare the data for API request
    input_data = {
        "clump_thickness": clump_thickness,
        "uniformity_of_cell_size": uniformity_of_cell_size,
        "uniformity_of_cell_shape": uniformity_of_cell_shape,
        "marginal_adhesion": marginal_adhesion,
        "single_epithelial_cell_size": single_epithelial_cell_size,
        "bare_nuclei": bare_nuclei,
        "bland_chromatin": bland_chromatin,
        "normal_nucleoli": normal_nucleoli,
        "mitoses": mitoses,
    }

    # Make the API request
    response = requests.post(f"{base_url}/api/predict", json=input_data)

    if response.status_code == 200:
        prediction = response.json()
        # st.write(f"The prediction is {prediction['label']} (Class: {prediction['prediction']})")
        st.success(f"The prediction is a {prediction['label']} tumor (Class: {prediction['prediction']})",
                   icon=":material/thumb_up:")
        rain(emoji="🎈", font_size=54, falling_speed=5, animation_length="infinite", )
    else:
        print(response)
        st.write("Error: Could not retrieve prediction. Please try again.")

# Run the Streamlit App
# streamlit run app.py
