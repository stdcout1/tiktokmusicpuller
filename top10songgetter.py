from TikTokApi import TikTokApi
from moviepy.editor import *
import requests
import sys
import os
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}



api = TikTokApi.get_instance()

trending = api.trending(count=20, custom_verifyFp="")
L = []
for tiktok in trending:
    # Prints the id of the tiktok
    video_url = tiktok['music']['playUrl']
    name = tiktok['music']['title']

    print(video_url)

    r = requests.get(video_url, headers=headers, allow_redirects=True)

    if r.status_code != 200:
        print('Bad request to no watermark video server. Status code: {}'.format(r.status_code))
        sys.exit(1)

    filename = 'music\\{}.mp4'.format(name)

    with open(filename, 'wb') as f:
        f.write(r.content)

for root, dirs, files in os.walk("music"):
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)
final_clip = concatenate_videoclips(L)
final_clip.to_videofile("output.mp4", fps=24, remove_temp=False)


