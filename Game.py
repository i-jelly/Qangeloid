# -*- coding:utf-8 -*-
import Music
#import sys
#from datetime import datetime, timedelta
#from pixivpy3 import *
import random
import os
#from PIL import Image

#_PASSWORD = "5bkk8pCq387B_Ts"
#_USERNAME = "hoshijiro@i-jelly.com"
#api = ByPassSniApi()
#api.require_appapi_hosts()
#api.set_accept_language('en-us')
#api.login(_USERNAME, _PASSWORD)
#json_result = api.illust_ranking('day', date=(datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'))

class Config:

    #if sys.version_info >= (3, 0):
    #    import imp
    #    imp.reload(sys)
    #else:
    #    reload(sys)
    #    sys.setdefaultencoding('utf8')
    #sys.dont_write_bytecode = True
    
    
    ListenGroup = ["963031509","671735106","209010051"]
    Admin = ["760658265"]
    GuaranS = 20
    GuaranSS = 50
    PicList = []
    LotOnceCost = 100
    LotTenCost = 1000
    OrderMusicCost = 10
    SChance = 0.05
    SSChance = 0.01
    AllowSpeak = True
    AllowRepeat = True
    SignRewardMin = 500
    SignRewardMax = 1000
    NorChance = 0.2
    NorUserLevel = 0
    PremiumUserLevel = 1
    AdminUserLevel = 5
    LowFavorLevelThres = 100
    MidFavorLevelThres = 500
    HigFavorLevelThres = 1000
    NoFavorFailRate = 0.1
    LowFavorFailRate = 0.2
    MidFavorFailRate = 0.05
    HigFavorBserRate = 0.2
    VoiceRate = 0.5
    LotFavor = 10
    LowFavorReject = "搭嘎,口都瓦路！"
    LowFavorRandReply = {
        "ja":["吾輩の名前はムラサメ。",
            "よろしく頼むぞ"],
        "cn":["吾辈的名字是丛雨",
            "多多指教了哦"],
        "vo":["reply/mur002_002.silk"]
    }
    MidFavorRandReply = {
        "ja":["吾輩に噓を吐いたのか、ご主人",
            "だから、吾輩で遊ぶでない、ご主人",
            "何だか、呆けておるようだな、ご主人",
            "ご主人、ふらぐを立てすぎじゃ…たいがいにせんと、今に神罰が下るぞ",
            "む、ご主人はわかっておらんな"],
        "cn":["居然敢欺骗吾辈啊，主人",
            "所以说，不要把吾辈当玩具，主人",
            "怎么感觉在发呆呢，主人",
            "主人FLAG立得太多了。再不收手的话，吾辈可就给你降下神罚咯",
            "姆，主人还真是一点都不上道啊"],
        "vo":["reply/mur001_054.silk","reply/mur001_059.silk",]
    }
    HigFavorRandReply = {
        "ja":["何か悩みでもあるなら、申してみよ",
            "あうっ、はっきり言わないでくれ…顔から火が出そうじゃ…",
            "い、いいかげんに察してくれ、ご主人",
            "…ん？どうしていきなり吾輩の頭を撫でるのだ、ご主人",
            "吾輩はもう諦める。そのままのご主人を受け入れしかない"],
        "cn":["如果有什么烦恼的话，说出来吧。",
            "啊呜，别说得太直接啊。。。",
            "差，差不多给我注意到啊，主人",
            "嗯？为何要突然摸吾辈的头啊，主人",
            "吾辈已经放弃了，只能接受这样的主人了"],
        "vo":["reply/mur001_058.silk","reply/mur001_062.silk","reply/mur001_065.silk"]
    }
    
    
    
    GeldName = "水晶"
    CommenReply = "略略略"
    RejectFavor = "呸"
    Store = {"963031509":["",0],"671735106":["",0],"209010051":["",0]}

    def __init__(self):
        super().__init__()
        _li = os.listdir("./pixiv/")
        for i in _li:
            self.PicList.append(i)
        #api.require_appapi_hosts()
        #api.set_accept_language('en-us')
        #api.login(_USERNAME, _PASSWORD)
        #json_result = api.illust_ranking('day', date=(datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'))

class Lotto:
    def __init__(self):
        super().__init__()

    def LotOnce(self,group,qq,li,chance,gar = None):
        Base = []
        Normal = []
        S = []
        SS = []
        for i in li:
            if i[3] == 4:
                SS.append(i)
            elif i[3] == 3:
                S.append(i)
            elif i[3] == 2:
                Normal.append(i)
            else:
                Base.append(i)
        if(isinstance(li,list)):
            if(gar == "SS"): return "触发SSR保底",random.choice(SS)
            elif(gar == "S"): return "触发SR保底",random.choice(S)
            _thistime = random.random()
            if(_thistime <= chance[0]):
                _ret = random.choice(SS)
                return _ret[1],_ret
            elif(_thistime <= chance[0] + chance[1]):
                _ret = random.choice(S)
                return _ret[1],_ret
            elif(_thistime <= chance[0] + chance[1] + chance[2]):
                _ret = random.choice(Normal)
                return _ret[1],_ret
            _ret = random.choice(Base)
            return _ret[1],_ret
        return "ERROR notice",False

    def LotTen(self,group,qq,li,chance):
        return "path","notice"

class Others:
    def __init__(self):
        super().__init__()

    def OrderMusic(self,group,qq,msg):
        _reply = Music.Music.GetMusic(None,group,qq,msg)
        if(not _reply):
            return "[CQ:at,qq={}]找不到歌曲".format(qq)
        return "[CQ:music,type=163,id={}]".format(_reply)

    def GetSeTu(self,group,qq):
        #illust = random.choice(json_result.illusts)
        #api.download(illust.image_urls.large,name = str(illust.title) + ".webp",prefix = "./data/image/pixiv/",replace = True)
        #img = Image.open("./data/image/pixiv/" + str(illust.title) + ".webp")
        #img.save("./data/image/pixiv/" + str(illust.title) + ".jpg")
        #return "[CQ:image,file=pixiv/{}.jpg]".format(str(illust.title))
        #return "[CQ:image,file={}]".format("FA5C6F804BA13E75F9716CF56CF0E84D.jpg")
        return "色图"

    def GiveGeld(self,group,qq,msg):
        return msg
    