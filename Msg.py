# -*- coding:utf-8 -*-
import Auth
import Reg
import random
import Sql
import Search
import Game

class GroupHandler:
    def __init__(self):
        super().__init__()
        self.Piclist = []

    def onNormalMsg(self,group,qq,msg):
        @Auth.AuthUserFavorLevel
        def revOrder(group,qq,msg,lev):
            if(lev > 3):
                if(random.random() < Game.Config.HigFavorBserRate):
                    if(random.random() > Game.Config.VoiceRate):
                        return "[CQ:record,file={},magic=false]".format(random.choice(Game.Config.HigFavorRandReply["vo"]))
                    return "[CQ:at,qq={}]{}".format(qq,random.choice(Game.Config.HigFavorRandReply["cn"]))
            elif(lev > 2):
                if(random.random() < Game.Config.MidFavorFailRate):
                    if(random.random() > Game.Config.VoiceRate):
                        return "[CQ:record,file={},magic=false]".format(random.choice(Game.Config.MidFavorRandReply["vo"]))
                    return "[CQ:at,qq={}]{}".format(qq,random.choice(Game.Config.MidFavorRandReply["cn"]))
            elif(lev > 1):
                if(random.random() < Game.Config.LowFavorFailRate):
                    if(random.random() > Game.Config.VoiceRate):
                        return "[CQ:record,file={},magic=false]".format(random.choice(Game.Config.LowFavorRandReply["vo"]))
                    return "[CQ:at,qq={}]{}".format(qq,random.choice(Game.Config.LowFavorRandReply["cn"]))
            return Game.Config.CommenReply

        return revOrder(group,qq,msg,1)

    def onOrderMsg(self,group,qq,msg):
        @Auth.AuthUserFavorLevel
        def revOrder(group,qq,msg,lev):
            if(msg == r"签到"):
                if(Sql.User.renewSign(None,group,qq)):
                    _add = random.randint(Game.Config.SignRewardMin,Game.Config.SignRewardMax)
                    Sql.User.setCash(None,group,qq,int(Sql.User.getCash(None,group,qq)) + _add)
                    return "[CQ:at,qq={}]签到成功~获得{}{}".format(qq,_add,Game.Config.GeldName)
                return "[CQ:at,qq={}]已经签过到了".format(qq)
            elif(msg[:2] == r"抽奖"):
                return random.randint(1,10)
            elif(msg[:2] == r"搜索"):
                if("#" not in msg): return "错误指令"
                return Search.moeGirl.getSearchContent(None,msg.split("#")[1])
            elif(msg[:7] == r"我们的关系如何"):
                if(lev > 2):
                    return "[CQ:at,qq={}]是{}的{}".format(qq,Sql.User.getCalled(None,group,qq),Sql.User.getCall(None,group,qq))
                return Game.Config.RejectFavor
            elif(msg[:4] == r"我是你的"):
                if(lev > 2):
                    _name = msg[4:].strip()
                    if(len(_name) >= 2):
                        Sql.User.setCall(None,group,qq,_name)
                        return "[CQ:at,qq={}]好的{}~".format(qq,_name)
                    return "[CQ:at,qq={}]是什么呢?".format(qq)
                return Game.Config.RejectFavor
            elif(msg[:4] == r"你是我的"):
                if(lev > 2):
                    _name = msg[4:].strip()
                    if(len(_name) >= 2):
                        Sql.User.setCalled(None,group,qq,_name)
                        return "[CQ:at,qq={}]{}知道了~".format(qq,_name)
                    return "[CQ:at,qq={}]是什么呢?".format(qq) 
                return Game.Config.RejectFavor
            elif(msg[:2] == r"单抽"):
                if(msg == r"单抽"): return "错误命令"
                Sql.User.addFavor(None,group,qq,Game.Config.LotFavor)
                if("＃" in msg) :_pool = msg.split("＃")[1]
                else:_pool = msg.split("#")[1]
                _addonreply = ""
                _rate = random.random()
                if(lev > 3):
                    if(_rate < Game.Config.HigFavorBserRate):
                        _addonreply = random.choice(Game.Config.HigFavorRandReply["cn"]) + "\n"
                elif(lev > 2):
                    if(_rate < Game.Config.MidFavorFailRate):
                        _addonreply = random.choice(Game.Config.MidFavorRandReply["cn"]) + "\n"
                elif(lev > 1):
                    if(_rate < Game.Config.LowFavorFailRate):
                        _addonreply = random.choice(Game.Config.LowFavorRandReply["cn"]) + "\n"
                else:
                    if(random.random() < Game.Config.NoFavorFailRate):
                        return Game.Config.LowFavorReject
                if(_pool in Reg.SpecialMsg.Card):
                    _int = int(Sql.User.getCash(None,group,qq))
                    if(_int >= Reg.SpecialMsg.Card[_pool][4]):
                        if(not Reg.SpecialMsg.Card[_pool][3]): return "[CQ:at,qq={}]卡池未开放".format(qq)
                        if(_pool not in Reg.SpecialMsg.Sys): return "[CQ:at,qq={}]卡池错误".format(qq)
                        if(Sql.User.setLastSS(None,group,qq,0) == 1):
                            _rpy,ret = Game.Lotto.LotOnce(None,group,qq,Reg.SpecialMsg.Sys[_pool],Reg.SpecialMsg.Card[_pool][:3],"SS")
                            Sql.User.setLastSS(None,group,qq,-1)
                        elif(Sql.User.setLastS(None,group,qq,0) == 1):
                            _rpy,ret = Game.Lotto.LotOnce(None,group,qq,Reg.SpecialMsg.Sys[_pool],Reg.SpecialMsg.Card[_pool][:3],"S")
                            Sql.User.setLastS(None,group,qq,-1)
                        else:
                            Sql.User.setLastSS(None,group,qq,1)
                            Sql.User.setLastS(None,group,qq,1)
                            _rpy,ret = Game.Lotto.LotOnce(None,group,qq,Reg.SpecialMsg.Sys[_pool],Reg.SpecialMsg.Card[_pool][:3])
                        if(ret):
                            Sql.User.setCash(None,group,qq,_int - Reg.SpecialMsg.Card[_pool][4])
                            if(not Sql.User.hasAva(None,group,qq,_pool,ret[1])):
                                Sql.User.addAva(None,group,qq,_pool,ret[1])
                            Sql.User.addHis(None,group,qq,_pool,ret[1])
                            return "[CQ:at,qq={}]\n[CQ:image,file={}]\n{}".format(qq,ret[2],_rpy) + "\n" + _addonreply                         
                        return "[CQ:at,qq={}]卡池错误".format(qq)
                    return "[CQ:at,qq={}]余额不足".format(qq)
                return "[CQ:at,qq={}]卡池不存在".format(qq)
            elif(msg[:2] == r"十连"):
                if(msg == r"十连"): return "错误命令"
                if("＃" in msg) :_pool = msg.split("＃")[1]
                else:_pool = msg.split("#")[1]
                Sql.User.addFavor(None,group,qq,Game.Config.LotFavor * 10)
                times = 10
                _addonreply = ""
                _rate = random.random()
                if(lev > 3):
                    if(_rate < Game.Config.HigFavorBserRate):
                        _addonreply = random.choice(Game.Config.HigFavorRandReply["cn"]) + "\n"
                        times = 11
                elif(lev > 2):
                    if(_rate < Game.Config.MidFavorFailRate):
                        _addonreply = random.choice(Game.Config.MidFavorRandReply["cn"]) + "\n"
                elif(lev > 1):
                    if(_rate < Game.Config.LowFavorFailRate):
                        _addonreply = random.choice(Game.Config.LowFavorRandReply["cn"]) + "\n"
                        times = 9
                else:
                    if(random.random() < Game.Config.NoFavorFailRate):
                        return Game.Config.LowFavorReject
                if(_pool in Reg.SpecialMsg.Card):
                    _int = int(Sql.User.getCash(None,group,qq))
                    if(_int >= Reg.SpecialMsg.Card[_pool][4] * 10):
                        if(not Reg.SpecialMsg.Card[_pool][3]): return "[CQ:at,qq={}]卡池未开放".format(qq)
                        if(_pool not in Reg.SpecialMsg.Sys): return "[CQ:at,qq={}]卡池错误".format(qq)
                        zus = ""
                        _img = ""
                        for i in range(times):
                            if(Sql.User.setLastSS(None,group,qq,0) == 1):
                                _rpy,ret = Game.Lotto.LotOnce(None,group,qq,Reg.SpecialMsg.Sys[_pool],Reg.SpecialMsg.Card[_pool][:3],"SS")
                                Sql.User.setLastSS(None,group,qq,-1)
                            elif(Sql.User.setLastS(None,group,qq,0) == 1):
                                _rpy,ret = Game.Lotto.LotOnce(None,group,qq,Reg.SpecialMsg.Sys[_pool],Reg.SpecialMsg.Card[_pool][:3],"S")
                                Sql.User.setLastS(None,group,qq,-1)
                            else:
                                Sql.User.setLastSS(None,group,qq,1)
                                Sql.User.setLastS(None,group,qq,1)
                                _rpy,ret = Game.Lotto.LotOnce(None,group,qq,Reg.SpecialMsg.Sys[_pool],Reg.SpecialMsg.Card[_pool][:3])
                            if(ret):
                                Sql.User.setCash(None,group,qq,_int - Reg.SpecialMsg.Card[_pool][4] * 10)
                                zus = zus + _rpy + ","
                                _img = _img + "[CQ:image,file={}]".format(ret[2])
                                if(not Sql.User.hasAva(None,group,qq,_pool,ret[1])):
                                    Sql.User.addAva(None,group,qq,_pool,ret[1])
                                Sql.User.addHis(None,group,qq,_pool,ret[1])
                        return "[CQ:at,qq={}]\n{}\n{}\n{}".format(qq,_img,zus,_addonreply)
                    return "[CQ:at,qq={}]余额不足".format(qq)
                return "[CQ:at,qq={}]卡池不存在".format(qq)
            elif(msg[:2] == r"点歌"):
                _int = int(Sql.User.getCash(None,group,qq))
                if(_int >= Game.Config.OrderMusicCost):
                    Sql.User.setCash(None,group,qq,_int - Game.Config.OrderMusicCost)
                    return Game.Others.OrderMusic(None,group,qq,msg[2:])
                return "[CQ:at,qq={}]余额不足".format(qq)
            elif(msg == r"我的余额"):
                return "[CQ:at,qq={}]你的余额为{}{}".format(qq,int(Sql.User.getCash(None,group,qq)),Game.Config.GeldName) 
            elif(msg == r"来点好康的"):
                #return Game.Others.GetSeTu(None,group,qq)
                return "[CQ:image,file={}]".format("./pixiv/" + random.choice(self.Piclist))
            elif(msg[0:4] == r"赠送水晶"):
                if (Game.Others.GiveGeld(None,group,qq,msg[4:])):
                    return "[CQ:at,qq={}]赠送成功~".format(qq)
                return "[CQ:at,qq={}]赠送失败".format(qq)
            elif(msg == r"我的好感"):
                return "[CQ:at,qq={}]好感度是{}".format(qq,Sql.User.getFavor(None,group,qq))
            elif(msg == r"我的保底"):
                return "[CQ:at,qq={}]你的SR保底还有{}发,你的SSR保底还有{}发".format(qq,Sql.User.setLastS(None,group,qq,0),Sql.User.setLastSS(None,group,qq,0))
            elif(msg[:4] == r"我的角色"):
                if(msg == r"我的角色"): return "错误命令"
                _ty = msg.split("#")[1]
                if(_ty in Reg.SpecialMsg.Sys):
                    _rep = ""
                    ava = Sql.User.getCards(None,group,qq,_ty)
                    for i in ava:
                        _rep = _rep + i + "\n"
                    _rep = _rep + "共{}张{}角色卡".format(len(ava),_ty)
                else:
                    _rep = "错误卡池"
                return _rep
            return False
        
        return revOrder(group,qq,msg,1)

    def onAdminMsg(self,group,qq,msg):
        @Auth.AuthAdminUser
        def revAdmin(group,qq,msg):
            if(msg == r"mua" and not Game.Config.AllowSpeak):
                Game.Config.AllowSpeak = True
                return Reg.SpecialMsg.Admin[0][2]
            elif(msg == r"口球" and Game.Config.AllowSpeak):
                Game.Config.AllowSpeak = False
                return Reg.SpecialMsg.Admin[1][2]
            elif(msg == r"开启复读" and not Game.Config.AllowRepeat):
                Game.Config.AllowRepeat = True
                return Reg.SpecialMsg.Admin[2][2]
            elif(msg == r"打断复读" and Game.Config.AllowRepeat):
                Game.Config.AllowRepeat = False
                return Reg.SpecialMsg.Admin[3][2]
            return Game.Config.CommenReply

        return revAdmin(group,qq,msg)

    def onFavorMsg(self,group,qq,msg):

        @Auth.AuthHighFavorLevel
        def HighFavor(group,qq,msg):
            return msg
        @Auth.AuthMidFavorLevel
        def MidFavor(group,qq,msg):
            return msg
        @Auth.AuthLowFavorLevel
        def LowFavor(group,qq,msg):
            return msg

        for i in Reg.SpecialMsg.Favor:
            if(i[1] == msg):
                if(i[2] == 1):
                    _rep = LowFavor(group,qq,msg)
                    if(not(_rep)): return random.choice(i[4])
                    return random.choice(i[3])
                elif(i[2] == 2):
                    _rep = MidFavor(group,qq,msg)
                    if(not(_rep)): return random.choice(i[4])
                    return random.choice(i[3])
                elif(i[2] == 3):
                    _rep = HighFavor(group,qq,msg)
                    if(not(_rep)): return random.choice(i[4])
                    return random.choice(i[3])
                else: return ""
        #return HighFavor(group,qq,msg)

class PrivateHandler:
    def __init__(self):
        super().__init__()

    def onNormalMsg(self,qq,msg):
        return "略略略"

    def onOrderMsg(self,qq,msg):
        return msg

    def onAdminMsg(self,qq,msg):
        return msg

    def onFavorMsg(self,qq,msg):
        
        @Auth.AuthHighFavorLevel
        def HighFavor(qq,msg):
            return msg
        @Auth.AuthMidFavorLevel
        def MidFavor(qq,msg):
            return msg
        @Auth.AuthLowFavorLevel
        def LowFavor(qq,msg):
            return msg

        return HighFavor(qq,msg)