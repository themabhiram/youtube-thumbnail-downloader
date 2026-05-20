import requests
import re
import os
from colorama import Fore, Style, init

init(autoreset=True)

def get_video_id(url):
    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"embed/([a-zA-Z0-9_-]{11})"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


print(Fore.CYAN + "=" * 50)
print(Fore.YELLOW + "- YOUTUBE THUMBNAIL DOWNLOADER")
print(Fore.GREEN + "- Created by: ABHIRAM")
print(Fore.MAGENTA + "- Instagram: themabhiram (https://www.instagram.com/themabhiram/)")
print(Fore.CYAN + "=" * 50)


while True:
    url = input(Fore.WHITE + "\nEnter YouTube URL (or type 'exit'): ")

    if url.lower() == "exit":
        print(Fore.YELLOW + "Exiting...")
        break

    video_id = get_video_id(url)

    if not video_id:
        print(Fore.RED + "Invalid YouTube URL ❌")
        continue

    save_path = input(Fore.WHITE + "Enter folder path (e.g. Desktop path): ")

    if not os.path.exists(save_path):
        print(Fore.RED + "Invalid folder path ❌")
        continue

    print(Fore.BLUE + "Downloading thumbnail...")

    thumb_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    res = requests.get(thumb_url)

    if res.status_code != 200:
        thumb_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        res = requests.get(thumb_url)

    file_path = os.path.join(save_path, f"{video_id}.jpg")

    with open(file_path, "wb") as f:
        f.write(res.content)

    print(Fore.GREEN + f"Thumbnail saved at: {file_path} ✅")