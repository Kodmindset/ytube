import streamlit as st
import yt_dlp
import os

st.title("🎥 YouTube Downloader")

url = st.text_input("Enter YouTube URL:")

if st.button("Download"):
    if url.strip() == "":
        st.warning("⚠️ Please enter a valid YouTube URL.")
    else:
        # Make a temporary downloads folder
        os.makedirs("downloads", exist_ok=True)

        ydl_opts = {
            # 'format': 'bv*+ba/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'force_generic_extractor': False,
            'noplaylist': True
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            st.success(f"✅ Download complete! File: {os.path.basename(filename)}")

            # Provide download button for the user
            with open(filename, "rb") as f:
                st.download_button(
                    label="⬇️ Download Video to your computer",
                    data=f,
                    file_name=os.path.basename(filename),
                    mime="video/mp4"
                )

        except Exception as e:
            st.error(f"❌ Error: {e}")
