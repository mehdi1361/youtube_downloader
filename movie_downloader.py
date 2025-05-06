from pytube import YouTube

def main():
    video_url = 'https://www.youtube.com/watch?v=nYXVvK-Wmn0&ab_channel=freeCodeCamp.org'
    yt = YouTube(video_url)
    print(f"Title: {yt.title}")
    print(f"Views: {yt.views}")
    print(f"Length: {yt.length} seconds")
    
    # Download the video
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(output_path='videos', filename=f"{yt.title}.mp4") # type: ignore # ignore
    print("Video downloaded successfully!")

main()