# -*- coding:utf-8 -*-
import urllib
import requests
import time
import json

url = "http://music.163.com/song/media/outer/url?id="
Header = {"Cookie":"_ntes_nnid=e2293b620c4dcb26156018bccce50b8f,1579011552641; _ntes_nuid=e2293b620c4dcb26156018bccce50b8f; NNSSPID=87d2f64e135a44fa8e2bc40c5ac4a020; UM_distinctid=16fa4bbf1a34ef-0b928af0d376a7-c383f64-144000-16fa4bbf1a451a; mail_psc_fingerprint=025e06bcbde6269bf8a238a760653459; JSESSIONID-WYYY=v9dzJGycaDcfbU3BA%2Fe%2F5gn1hmzTsBYCHWxBV%5Cbu9P0QP661sfF2TNOO4JnSq%2F4zM5pN4e6c%5CZc2%2Fp4nEtbB84HwQm1GB1Tc69HYkne6Suj8i%2Bo3Tkdy4u%2FluB8ZNlu1N27nfsSv9BW3oPZpswXtnEh9Xe4k6zR%5C1YTaqKw1IqOVH3gh%3A1579018600035; _iuqxldmzr_=32; WM_NI=DXUCECoen22I%2FB5DWE4W6tl9dIa1BCB%2BRQMzXvFl0ohrSnRelo8xkM63kkzmXnInaAHF3macmsEKsJHrigux8yB1SwffFUS6%2FcHcecPXtZw2lWCwo2tn%2BkRJ6tMfoX7FMkE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed9f76d948d8bbae850aeb48fa6d14b838b8faebb7fb8b4a98bf45fa9910099d62af0fea7c3b92a88889ba4c849adbba2d3b143ed9efba5d64ff889fa95ef33a897afd2c14982f59eb2d0729caa8a8db365acae9d8fd16fb0b1f899ea47f6eda58cf9679cb2878fe44b8c9afd8ee469afad8bacf2428caea788f874fca78ed2d27da6ba8ab6d23eedbd8884e8699488bcbbf63ab0898d98ee3ab8b2e58cd142f6ac8387ee54f59a838cc837e2a3; WM_TID=SSiytp%2Bf1fJFFQUUBUJp%2F4lh3vVkfk1G; P_INFO=sakiruai@163.com|1579016927|0|mail163|00&99|null&null&null#zhj&330100#10#0#0|&0||sakiruai@163.com; nts_mail_user=sakiruai@163.com:-1:1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

class Music:
    def __init__(self):
        super().__init__()
        self.name = name
        opener = urllib.request.build_opener()
        opener.addheaders = [('Cookie', "_ntes_nnid=e2293b620c4dcb26156018bccce50b8f,1579011552641; _ntes_nuid=e2293b620c4dcb26156018bccce50b8f; NNSSPID=87d2f64e135a44fa8e2bc40c5ac4a020; UM_distinctid=16fa4bbf1a34ef-0b928af0d376a7-c383f64-144000-16fa4bbf1a451a; mail_psc_fingerprint=025e06bcbde6269bf8a238a760653459; JSESSIONID-WYYY=v9dzJGycaDcfbU3BA%2Fe%2F5gn1hmzTsBYCHWxBV%5Cbu9P0QP661sfF2TNOO4JnSq%2F4zM5pN4e6c%5CZc2%2Fp4nEtbB84HwQm1GB1Tc69HYkne6Suj8i%2Bo3Tkdy4u%2FluB8ZNlu1N27nfsSv9BW3oPZpswXtnEh9Xe4k6zR%5C1YTaqKw1IqOVH3gh%3A1579018600035; _iuqxldmzr_=32; WM_NI=DXUCECoen22I%2FB5DWE4W6tl9dIa1BCB%2BRQMzXvFl0ohrSnRelo8xkM63kkzmXnInaAHF3macmsEKsJHrigux8yB1SwffFUS6%2FcHcecPXtZw2lWCwo2tn%2BkRJ6tMfoX7FMkE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed9f76d948d8bbae850aeb48fa6d14b838b8faebb7fb8b4a98bf45fa9910099d62af0fea7c3b92a88889ba4c849adbba2d3b143ed9efba5d64ff889fa95ef33a897afd2c14982f59eb2d0729caa8a8db365acae9d8fd16fb0b1f899ea47f6eda58cf9679cb2878fe44b8c9afd8ee469afad8bacf2428caea788f874fca78ed2d27da6ba8ab6d23eedbd8884e8699488bcbbf63ab0898d98ee3ab8b2e58cd142f6ac8387ee54f59a838cc837e2a3; WM_TID=SSiytp%2Bf1fJFFQUUBUJp%2F4lh3vVkfk1G; P_INFO=sakiruai@163.com|1579016927|0|mail163|00&99|null&null&null#zhj&330100#10#0#0|&0||sakiruai@163.com; nts_mail_user=sakiruai@163.com:-1:1"),
                            ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36")]
        urllib.request.install_opener(opener)

    def GetMusic(self,group,qq,msg):
        _res = requests.post("http://music.163.com/api/search/pc?limit=1&type=1&s={}".format(msg),headers=Header)
        _json = json.loads(_res.text)
        try:
            _reply = int(_json.get("result").get("songs")[0].get("id"))
        except:
            return False
        return _reply
