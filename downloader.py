#!/usr/bin/env python3
import youtube_dl
import pandas


def download_vid(url, index):
    if index:
        output_string = f"./downloads/{index} - %(title)s - %(artist)s.%(ext)s"
    else:
        output_string = f"./downloads/%(title)s - %(artist)s.%(ext)s"

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'restrictfilenames': True,
        'download_archive': './archive/archive.txt',
        'outtmpl': output_string}

    try:
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        ydl.download([url])
    except Exception as error:
        raise error


def main():
    file = pandas.read_csv('csv_to_download.csv')
    urls_list = file['URL'].tolist()
    total_songs = len(urls_list)

    downloaded_songs = 0
    errors = 0

    for i, url in enumerate(reversed(urls_list)):
        try:
            download_vid(url, i+1)
            downloaded_songs += 1
        except Exception as error:
            print(f"Song number {i + 1} could not be loaded")
            print(error)
            errors += 1

        print(f"Song number {i+1} of {total_songs}. ({round(((i+1)/total_songs)*100, 2)}%).\n"
              f"Songs downloaded: {downloaded_songs}\n"
              f"Errors: {errors}\n")


if __name__ == "__main__":
    main()
