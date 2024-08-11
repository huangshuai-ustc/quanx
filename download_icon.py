import time
import requests
from bs4 import BeautifulSoup

headers = {}
urls = [
    'https://raw.githubusercontent.com/Orz-3/mini/master/Color/Global.png',
    'https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Color/Apple.png',
    'https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Color/bilibili.png',
    'https://raw.githubusercontent.com/Orz-3/mini/master/Color/Streaming.png',
    'https://raw.githubusercontent.com/Orz-3/mini/master/Color/Final.png',
    'https://raw.githubusercontent.com/huangshuai-ustc/quanx/main/iconfonts/openai.ico',
    'https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Color/Auto.png',
    'https://raw.githubusercontent.com/Orz-3/mini/master/Color/HK.png',
    'https://raw.githubusercontent.com/Orz-3/mini/master/Color/TW.png',
    'https://raw.githubusercontent.com/Orz-3/mini/master/Color/JP.png',
    'https://raw.githubusercontent.com/Orz-3/mini/master/Color/SG.png',
    'https://raw.githubusercontent.com/Orz-3/mini/master/Color/US.png',
    'https://www.google.com/favicon.ico']
for url in urls:
    print(url)
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 将内容写入文件
        with open('D:/ProgramData/Codes/GitHub/quanx/iconfonts/' + url.split('/')[-1], 'wb') as file:
            file.write(response.content)
        print(f"File saved")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
