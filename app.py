import streamlit as st
import yt_dlp

st.title("🎥 YouTube Downloader")

url = st.text_input("Enter YouTube URL:")

if st.button("Download"):
    if url.strip() == "":
        st.warning("⚠️ Please enter a valid YouTube URL.")
    else:
        ydl_opts = {
   # 'format': 'bv*+ba/best',
    'outtmpl': '%(title)s.%(ext)s',
    'force_generic_extractor': False,  # ✅ Force using full metadata extractor
    'noplaylist': True                 # Don't treat as playlist
}

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            st.success(f"✅ Download complete! File saved as: {filename}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
