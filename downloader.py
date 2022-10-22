#!/usr/bin/env python3
import youtube_dl
import pandas


def download_vid(url, index):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'restrictfilenames': True,
        'outtmpl': f"./downloads/%(title)s - %(artist)s.%(ext)s"}
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])


def main():
    urls = pandas.read_csv('csv_to_download.csv')
    urls_list = urls['URL'].tolist()
    count = 0
    for url in urls.iterrows():
        current_url = url[1]['URL']
        download_vid(current_url)
        count += 1
        print(count)


if __name__ == "__main__":
    main()
