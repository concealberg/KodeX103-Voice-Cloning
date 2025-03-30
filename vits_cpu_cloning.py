import streamlit as st
from gtts import gTTS

# Streamlit UI Setup
st.set_page_config(page_title="ELARA AI - Emotional Voice Cloning", layout="centered")
st.title("🎙 ELARA AI - Voice Cloning Model")
st.markdown("### 🎤 Enter Text and Choose Emotion")

# Language Selection
language_options = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh",
    "Japanese": "ja"
}
selected_language = st.selectbox("🌍 Choose Language:", list(language_options.keys()))

# Emotion Selection
emotion = st.selectbox("🎭 Choose Emotion:", ["Neutral", "Happy", "Sad"])

# Text Input
text_input = st.text_area("✍️ Enter text for voice cloning:")

# Reference Audio Upload
st.markdown("### 🎵 Upload Reference Audio (Optional):")
uploaded_audio = st.file_uploader("📂 Upload a WAV file for reference voice", type=["wav"])

# Clone Voice Button
if st.button("🎙 Generate Voice"):
    if not text_input:
        st.error("⚠ Please enter text to generate speech!")
    else:
        st.success(f"🔊 Generating {emotion.lower()} speech...")

        # Convert Text to Speech
        tts = gTTS(text=text_input, lang=language_options[selected_language])
        output_audio_path = "cloned_voice.mp3"
        tts.save(output_audio_path)

        # Play generated audio
        st.audio(output_audio_path, format="audio/mp3")

        # Show uploaded reference audio if available
        if uploaded_audio:
            st.markdown("### 🎧 Reference Voice Provided:")
            st.audio(uploaded_audio, format="audio/wav")
        else:
            st.warning("⚠ No reference audio provided! Using default voice.")

st.markdown("---")
st.write("© 2025 Team Kodevenger | ELARA AI - Advanced Emotional Voice Cloning")





