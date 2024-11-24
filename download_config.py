import time
import requests
from typing import List

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'
}

filter_urls = [
    'https://raw.githubusercontent.com/ddgksf2013/Filter/master/NeteaseMusic.list',
    'https://raw.githubusercontent.com/ddgksf2013/Filter/master/Unbreak.list',
    'https://raw.githubusercontent.com/Cats-Team/AdRules/main/qx.conf',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/TikTok/TikTok.list',
    'https://github.com/blackmatrix7/ios_rule_script/raw/master/rule/QuantumultX/OpenAI/OpenAI.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Spotify/Spotify.list',
    'https://raw.githubusercontent.com/ddgksf2013/Filter/master/Streaming.list',
    'https://raw.githubusercontent.com/ddgksf2013/Filter/master/StreamingSE.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Apple/Apple.list',
    'https://raw.githubusercontent.com/VirgilClyne/GetSomeFries/main/ruleset/ASN.China.list',
    'https://whatshub.top/rule/WeChat.list',
    'https://raw.githubusercontent.com/ConnersHua/RuleGo/master/Surge/Ruleset/Proxy.list',
    'https://raw.githubusercontent.com/ddgksf2013/Filter/master/GoogleVoice.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/12306/12306.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/ABC/ABC.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AppleMusic/AppleMusic.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Bing/Bing.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/MeiTuan/MeiTuan.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Tencent/Tencent.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/XieCheng/XieCheng.list',
    'https://whatshub.top/rule/Alibaba.list']

rewrite_urls = [
    'https://whatshub.top/rewrite/wechatad.conf',
    'https://whatshub.top/rewrite/ZhihuBlock.conf',
    'https://whatshub.top/rewrite/biliad.conf',
    'https://whatshub.top/rewrite/doc.conf',
    'https://whatshub.top/rewrite/znz.conf',
    'https://whatshub.top/rewrite/nfc.conf',
    'https://whatshub.top/rewrite/adultraplus.conf',
    'https://raw.githubusercontent.com/thebestkyle323/Quantumult-x/main/WPSuperVIPuserCrack.js',
    'https://raw.githubusercontent.com/ddgksf2013/Rewrite/master/AdBlock/Bilibili.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/UnlockVip/Spotify.conf',
    'https://github.com/ddgksf2013/dev/raw/master/ForOwnUse.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/AdBlock/StartUp.conf',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/script/zheye/zheye.snippet',
    'https://github.com/app2smile/rules/raw/master/module/tieba-qx.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/AdBlock/Applet.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/AdBlock/YoutubeAds.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/AdBlock/Weibo.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/AdBlock/Ximalaya.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/AdBlock/Amap.conf',
    'https://raw.githubusercontent.com/ddgksf2013/Rewrite/refs/heads/master/AdBlock/NeteaseAds.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/Html/WebAdBlock.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/Html/Q-Search.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/Html/Douban.conf',
    'https://github.com/ddgksf2013/Rewrite/raw/master/AdBlock/XiaoHongShu.conf',
    'https://gist.githubusercontent.com/ddgksf2013/f43026707830c7818ee3ba624e383c8d/raw/baiduCloud.adblock.js',
    'https://raw.githubusercontent.com/ddgksf2013/Rewrite/master/Function/UnblockURLinWeChat.conf',
    'https://raw.githubusercontent.com/ddgksf2013/Rewrite/master/Html/General.conf',
    'https://raw.githubusercontent.com/Orz-3/QuantumultX/master/Netflix_ratings.conf',
    'https://raw.githubusercontent.com/id77/QuantumultX/master/rewrite/Youtube_CC.conf',
    'https://raw.githubusercontent.com/chavyleung/scripts/master/box/rewrite/boxjs.rewrite.quanx.conf',
    'https://raw.githubusercontent.com/w37fhy/QuantumultX/master/QuantumultX_Cookie.conf']

config_urls = ['https://github.com/ddgksf2013/Profile/raw/master/QuantumultX.conf']

task_urls = ['https://raw.githubusercontent.com/deezertidal/private/main/rumors.js',
             'https://raw.githubusercontent.com/deezertidal/private/main/appsdoor.js',
             'https://raw.githubusercontent.com/deezertidal/private/main/histoday.js',
             'https://raw.githubusercontent.com/deezertidal/private/main/rates.js',
             'https://raw.githubusercontent.com/deezertidal/private/main/lifeindex.js',
             'https://whatshub.top/plugin/movie.js',
             'https://raw.githubusercontent.com/KOP-XIAO/QuantumultX/master/Scripts/UI-Action.json',
             'https://raw.githubusercontent.com/KOP-XIAO/QuantumultX/master/Scripts/streaming-ui-check.js',
             'https://raw.githubusercontent.com/shufflewzc/faker/main/qx.json']

http_urls = ['https://raw.githubusercontent.com/chavyleung/scripts/master/chavy.box.js']

parser_urls = ['https://raw.githubusercontent.com/KOP-XIAO/QuantumultX/master/Scripts/resource-parser.js']


def main(urls: List[str], dir_name: str) -> None:
    for url in urls:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            time.sleep(1)
            file_name = f'D:/ProgramData/Codes/GitHub/quanx/{dir_name}/' + url.split('/')[-1]
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(r.text)
        else:
            print(r.status_code)
            print(url)


if __name__ == '__main__':
    main(urls=filter_urls, dir_name='Filter')
    main(urls=rewrite_urls, dir_name='Rewrite')
    main(urls=config_urls, dir_name='Config')
    main(urls=task_urls, dir_name='Task')
    main(urls=http_urls, dir_name='Http')
    main(urls=parser_urls, dir_name='Parser')
    print('All Done!')

