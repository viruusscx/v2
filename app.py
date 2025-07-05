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

custom_css = """
body {
    font-family: 'Poppins', sans-serif;
}

h1 {
    text-align: center;
    font-weight: 600;
    color: #FF4B2B;
    font-size: 2.2em;
}

.footer {
    text-align: center;
    font-size: 16px;
    color: #888;
    margin-top: 40px;
    font-style: italic;
    letter-spacing: 1px;
}
"""

with gr.Blocks(css=custom_css, title="YouTube Playlist Downloader") as demo:
    gr.Markdown("<h1>🎥 YouTube Playlist Downloader</h1>")
    url_input = gr.Text(label="Paste YouTube Playlist URL")
    output_file = gr.File(label="Download ZIP")

    with gr.Row():
        clear_btn = gr.Button("Clear")
        submit_btn = gr.Button("Submit", variant="primary")

    footer = gr.Markdown("<div class='footer'>✨ This web is made by <strong>AMAN AVTHARE</strong></div>")

    def start_download(url):
        return download_playlist(url)

    submit_btn.click(fn=start_download, inputs=url_input, outputs=output_file)
    clear_btn.click(lambda: "", outputs=url_input)

demo.launch()
