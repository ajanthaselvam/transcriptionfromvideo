from youtube_transcript_api import YouTubeTranscriptApi as yta
from pytube import YouTube
import webbrowser

def get_youtube_details():
    # Input the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the video title and thumbnail URL
    video_title = yt.title
    thumbnail_url = yt.thumbnail_url


    # Open the video in a web browser
    webbrowser.open(video_url)

# Display the video details
    print("Playing YouTube video:")
    print("Title:", video_title)
    print("Thumbnail URL:", thumbnail_url)


def get_youtube_timeframe():
    link = 'https://youtu.be/VI3f-GaRoIM?si=Ena18bvIK1y-0-j5?t=50s'
    id = link.split('/')
    vid_id = id[-1]

    data = yta.get_transcript(vid_id)
    print(data)

    final_data = ''
    for val in data:
        for key,value in val.items():
            if key == 'text':
                final_data += value
    process_data = final_data.splitlines()
    clean_data = ''.join(process_data)

    #print(clean_data)

def main():
    get_youtube_details()
    get_youtube_timeframe()

if __name__ == "__main__":
    main()
