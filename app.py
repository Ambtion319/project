# file: app.py
from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    output_path = "video.mp4"
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return f"Error: {e}"

    finally:
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == '__main__':
    app.run(debug=True)
