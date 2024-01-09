import requests
import json 
import re
import os
from pprint import pprint

url = r'https://www.bilibili.com/video/BV1nb4y137XE'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "Referer":"https://search.bilibili.com/all?keyword=%E8%AF%B4%E8%AF%B4%E8%AF%9D&from_source=webtop_search&spm_id_from=333.1007&search_source=3"
}

resp = requests.get(url = url, headers = headers)
# print(resp.text)
obj = re.compile(r'window.__playinfo__=(.*?)</script>', re.S)
html_data = obj.findall(resp.text)[0]
json_data = json.loads(html_data)
# pprint(json_data)
videos = json_data['data']['dash']['video']
video_url = videos[0]['baseUrl']

audios = json_data['data']['dash']['audio']
audio_url = audios[0]['baseUrl']

resp1 = requests.get(url = video_url, headers = headers)

with open('test.mp4', mode = 'wb') as f:
    f.write(resp1.content)

resp2 = requests.get(url = audio_url, headers = headers)

with open('test.mp3', mode = 'wb') as f:
    f.write(resp2.content)

command = r'ffmpeg -i test.mp4 -i test.mp3 -acodec copy -vcodec copy testout.mp4'
os.system(command = command)

print("下载完成！！！")