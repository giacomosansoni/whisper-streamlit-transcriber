# 🎤 YouTube Transcriber  
*A Streamlit app to download and transcribe YouTube audio using OpenAI Whisper.*  

![App Screenshot](Screenshot 2025-03-01 alle 21.06.19.png)

## Structure   
1. **Downloads audio from YouTube videos** using `yt-dlp`  
2. **Transcribes speech** using OpenAI’s **Whisper model**  
3. **Supports multiple languages** (English, Italian, German, French)  
4. **Allows users to download the transcription as a text file**  

---

## Installation  
To set up the project on your local machine, follow these steps:

### **1️⃣ Install FFmpeg (Required)**
FFmpeg is needed for processing and converting audio.

- **Windows**: Download and install [FFmpeg](https://ffmpeg.org/download.html), then add it to your system's PATH.  
- **Mac**: Install via Homebrew:
  ```bash
  brew install ffmpeg
  ```
- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```

### **2️⃣ Create a Virtual Environment (Optional, but Recommended)**
```bash
python -m venv venv
```

This creates a `.venv` folder in your current directory.

Now activate the Virtual Environment

- **macOS/Linux:**
  
```bash
source .venv/bin/activate
```

- **Windows:**
  
```cmd
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt.

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Streamlit App**
```bash
streamlit run streamlit_app.py
```

---

## Usage  
1️⃣ **Paste the YouTube link** into the text box  
2️⃣ **Select the transcription language**  
3️⃣ **Click "Transcribe"** to download and process the audio  
4️⃣ **View the transcription** directly in the app  
5️⃣ **Download the transcription** as a `.txt` file  

---

## Project Structure
```
📂 your-repository
│── 📜 README.md              # Project documentation
│── 📜 requirements.txt       # Dependencies
│── 📜 streamlit_app.py   # Streamlit app (main entry point)
│── 📜 notebook.ipynb     # Jupyter Notebook (for testing/experiments)
│── 📂 img                    # Images folder
│   │── 📸 screenshot.png     # Screenshot of the app

```

---

## Technologies Used  
- **Streamlit** → Interactive web interface  
- **yt-dlp** → YouTube audio extraction  
- **Whisper by OpenAI** → Speech-to-text transcription  
- **PyTorch** → Backend for Whisper model  
- **FFmpeg** → Audio processing (must be installed separately)  

---

❌ Long videos might take time to transcribe  

---
