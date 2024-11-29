import argparse
import subprocess
import os
from datetime import datetime

# Function to download video as MP3
def download_video_as_mp3(url, path, custom_name=None):
    if not url.strip():
        raise ValueError("No URL provided.")
    if not path.strip():
        path = os.getcwd()

    if not custom_name:
        custom_name = f"audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
    else:
        custom_name += ".mp3"

    try:
        output_path = os.path.join(path, custom_name)
        command = f"yt-dlp --extract-audio --audio-format mp3 -o '{output_path}' {url}"
        subprocess.run(command, shell=True, check=True)
        print(f"Audio downloaded to {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Download failed: {str(e)}")

# Main function to handle command-line arguments and process
def main():
    parser = argparse.ArgumentParser(description="Download audio as MP3 from a YouTube video.")
    parser.add_argument("url", help="URL of the YouTube video")
    parser.add_argument("--path", default="", help="Path to save the audio (leave empty for current directory)")
    parser.add_argument("--name", default="", help="Custom name for the audio file (without extension)")

    args = parser.parse_args()

    # Step 1: Download audio
    print("Downloading audio...")
    download_video_as_mp3(args.url, args.path, args.name)

if __name__ == "__main__":
    main()
