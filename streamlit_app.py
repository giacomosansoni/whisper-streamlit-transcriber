import streamlit as st
import yt_dlp
import whisper
import io
import os

st.set_page_config(page_title="Transcriber", page_icon="🤓", layout="centered")

# Persistent state for transcription
if "transcription" not in st.session_state:
    st.session_state.transcription = None

### DOWNLOAD AUDIO ###
def download_audio(url, output_filename="audio.m4a"):
    ydl_opts = {
        'format': 'm4a/bestaudio',  # Get the best audio in M4A format
        'outtmpl': output_filename,  # Set output filename
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

### TRANSCRIBE ###
def transcribe_audio(audio_file, model_size="small", language="it"):
    model = whisper.load_model(model_size)  # Load the Whisper model
    result = model.transcribe(audio_file, language=language)  # Transcribe
    return result["text"]

### MAIN ###
def main():
    st.title("Personal Transcriber")

    # Form for input
    with st.form(key='Inputs', border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            url = st.text_input("Paste the YouTube link here")
        with col2:
            language = st.selectbox("Choose the Language", ["English", "Italian", "German", "French"])

        submitted = st.form_submit_button("Transcribe", use_container_width=True)

    # If user submits a link
    if submitted and url:
        with st.spinner("Downloading and transcribing..."):
            # Step 1: Download the audio
            download_audio(url, output_filename="audio.m4a")

            # Step 2: Transcribe the audio
            transcription = transcribe_audio("audio.m4a", model_size="small", language=language)

            # Store transcription in session state so it persists
            st.session_state.transcription = transcription

    # Display transcription if available
    if st.session_state.transcription:
        st.subheader("Transcription")
        st.text_area("Transcribed Text", st.session_state.transcription, height=250)

        # Convert text into a file-like object for download
        text_file = io.BytesIO(st.session_state.transcription.encode("utf-8"))

        # Create columns with specific widths to control positioning
        col_download, col_spacer, col_reset = st.columns([2, 3, 2])  # Adjust ratios as needed

        # Download button in the left column
        with col_download:
            st.download_button(
                label="Download Transcription",
                data=text_file,
                file_name="transcription.txt",
                mime="text/plain",
            )

        # Reset button in the right column
        with col_reset:
            if st.button("Transcribe Another Link", type='primary'):
                # Delete audio file if it exists
                if os.path.exists("audio.m4a"):
                    os.remove("audio.m4a")
                    
                # Reset stored transcription
                st.session_state.transcription = None
                
                # Rerun app to clear input
                st.rerun()

if __name__ == "__main__":
    main()
