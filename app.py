import os, shutil
import gradio as gr

def download_playlist(url):
    folder = "yt_playlist"
    zip_file = "playlist_videos.zip"

    if os.path.exists(folder):
        shutil.rmtree(folder)
    if os.path.exists(zip_file):
        os.remove(zip_file)

    os.makedirs(folder, exist_ok=True)
    os.system(f'yt-dlp -f "bv*+ba/best" -o "{folder}/%(title)s.%(ext)s" "{url}"')
    os.system(f'zip -r {zip_file} {folder}')
    return zip_file

# 👇 Tell Gradio to use Render's port
port = int(os.environ.get("PORT", 7860))

demo = gr.Interface(
    fn=download_playlist,
    inputs=gr.Text(label="Paste YouTube Playlist URL"),
    outputs=gr.File(label="Download ZIP"),
    title="🎥 YouTube Playlist Downloader",
    description="Made by Aman Avthare"
)

demo.launch(server_name="0.0.0.0", server_port=port)
