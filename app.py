import streamlit as st
import requests


API_URL = "https://fastapi-backend-5c7d33b84556.herokuapp.com/predict"

def predict_note_authentication(variance, skewness, curtosis, entropy):
    try:
        payload = {
            "variance": float(variance),
            "skewness": float(skewness),
            "curtosis": float(curtosis),
            "entropy": float(entropy)
        }
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("prediction", "No prediction returned")
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    variance = st.text_input("Variance", "Type Here")
    skewness = st.text_input("Skewness", "Type Here")
    curtosis = st.text_input("Curtosis", "Type Here")
    entropy = st.text_input("Entropy", "Type Here")

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        st.success(f'The output is {result}')

    if st.button("About"):
        st.text("We don't follow the future. We build it!")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()





