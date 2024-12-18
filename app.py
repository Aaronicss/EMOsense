import streamlit as st
import joblib

# Load the trained model
pipeline = joblib.load('emotion_classifier.pkl')
st.set_page_config(
    page_title="EMOsense",
    page_icon="🎭",
)
# Streamlit interface
st.title("Welcome to EMOsense")
st.image("logo.png", width=200)
st.subheader("Enter a message to see its emotion classification.")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input text for prediction
text_input = st.text_area("Your Message:", height=70)  # Adjust height as needed

# Function to handle submit
def submit_input():
    # Make a prediction
    if text_input:
        prediction = pipeline.predict([text_input])

        # Append input and prediction to chat history
        st.session_state.chat_history.insert(0, ('You: ' + text_input, '🎭 Emotion: ' + prediction[0]))

        # Clear the text input box
        st.session_state.text_input = ""

# Layout with columns for buttons
col1, col2 = st.columns([3, 1])  # Adjust the column sizes as needed

with col1:
    # Submit button
    submit_button = st.button("Submit", on_click=submit_input)

with col2:
    try:
        clear_button = st.button("Clear Chat History", on_click=lambda: st.session_state.update({'chat_history': []}))
        if clear_button:
            st.experimental_rerun()
    except:
        pass

# Display chat history (most recent at the top)
st.subheader("Chat History")
if st.session_state.chat_history:
    for user_input, bot_response in st.session_state.chat_history:
        st.write(user_input)
        st.write(bot_response)
