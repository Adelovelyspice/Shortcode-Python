from pytube import YouTube

def download_youtube_video(url, path):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading {yt.title}...")
        stream.download(output_path=path)
        print("Download completed!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your desired YouTube video URL
path = "./downloads"  # Replace with your desired download directory
download_youtube_video(url, path)
