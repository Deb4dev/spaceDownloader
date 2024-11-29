
import subprocess
import os

def download_audio(url, output_folder):
   
    if not url.strip():
        raise ValueError("No URL provided.")
    if not output_folder.strip():
        output_folder = os.getcwd()

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Dynamic file naming template
    filename_template = os.path.join(output_folder, "%(title)s.%(ext)s")

    # yt-dlp command to download audio
    command = [
        "yt-dlp",
        "-f", "bestaudio",          # Best audio stream
        "--extract-audio",          # Extract audio only
        "--audio-format", "mp3",    # Convert audio to MP3
        "-o", filename_template,    # Dynamic naming with title
        url                         # YouTube URL
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Audio downloaded successfully and saved in: {output_folder}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error downloading audio: {e}")

# Example usage
if __name__ == "__main__":
    url = input("Enter the YouTube video or playlist URL: ").strip()
    output_folder = input("Enter the output folder (leave blank for current directory): ").strip()

    print("Starting download...")
    download_audio(url, output_folder)
    print("Download completed!")


