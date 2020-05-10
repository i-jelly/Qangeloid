# -*- coding:utf-8 -*-

import cqplus
import Auth
import Sql
import Game
import Reg
import Msg
import os


class MainHandler(cqplus.CQPlusHandler):
    _Rep = {}
    def __init__(self):
        super().__init__()
        self._Order = []
        self._Admin = []
        self.AllowSpeak = True
        self.AllowRepeat = True
        self.Piclist = []
        for j in Reg.SpecialMsg.Order:
            self._Order.append(j[1])
        for j in Reg.SpecialMsg.Admin:
            self._Admin.append(j[1])
        _li = os.listdir("./data/image/pixiv/")
        for i in _li:
            self.Piclist.append(i)

    def handle_event(self, event, params):
        #self.logging.debug(event)
        if(event == "on_enable"):
            for i in Game.Config.ListenGroup:
                if(not(Sql.Base.hasTable(self,i,"User"))):
                    Sql.Base.initTable(self,i)
                    self.logging.debug("CREATE SUC")
            self.logging.debug("ALL DONE")
        elif(event == "on_group_msg"):
            #复读机部分
            _msg = params["msg"]
            _qq = params["from_qq"]
            _group = params["from_group"]
            _in = False
            for k in Game.Config.ListenGroup:
                if(int(k) == _group):
                    _in = True
            if(not(_in)):
                return
            if(Game.Config.Store[str(_group)][0] == _msg and Game.Config.Store[str(_group)][1] != _qq and Game.Config.AllowSpeak and Game.Config.AllowRepeat):
                self.api.send_group_msg(_group,_msg)
                Game.Config.Store[str(_group)][0] = ""
                Game.Config.Store[str(_group)][1] = 0
                return
            elif(Game.Config.AllowRepeat):
                #self.api.send_group_msg(_group,Game.Config.Store[str(_group)][0])
                Game.Config.Store[str(_group)][0] = _msg
                
                Game.Config.Store[str(_group)][1] = _qq
            #路由部分，分发到Msg中对应处理函数
            
            if(len(_msg) > 21):
                if(_msg.strip()[:21] == "[CQ:at,qq=3178223002]"):
                    if(Sql.User.isExists(None,_group,_qq)): Sql.User.addFavor(None,_group,_qq,1)
                    Game.Config.Store[str(_group)][0] = ""
                    Game.Config.Store[str(_group)][1] = 0
                    _order = _msg[21:].strip()
                    for l in Reg.SpecialMsg.Admin:
                        if(_order == l[1]):
                            _reply = Msg.GroupHandler.onAdminMsg(self,_group,_qq,_order)
                            self.api.send_group_msg(_group,_reply)
                            return
                    if(Game.Config.AllowSpeak):
                        #self.logging.debug(_msg[21:])
                        if(_order == r"注册"):
                            if(Sql.User.isExists(self,_group,_qq)):
                                self.api.send_group_msg(_group,"[CQ:at,qq={}]已经注册了哦".format(_qq))
                            else:
                                if(Sql.User.addUser(self,_group,_qq)):
                                    self.api.send_group_msg(_group,"[CQ:at,qq={}]注册成功~".format(_qq))
                                else:
                                    self.api.send_group_msg(_group,"[CQ:at,qq={}]注册失败".format(_qq))
                            return
                        if(Sql.User.isExists(None,_group,_qq)):
                            _call = Sql.User.getCalled(None,_group,_qq)
                            if(_order[:len(_call)] == _call):
                                _order = _order[len(_call):].strip()
                        for l in Reg.SpecialMsg.Admin:
                            if(_order == l[1]):
                                Sql.User.addFavor(None,_group,_qq,1)
                                _reply = Msg.GroupHandler.onAdminMsg(self,_group,_qq,_order)
                                if(not _reply): return self.api.send_group_msg(_group,Game.Config.CommenReply)
                                self.api.send_group_msg(_group,_reply)
                                return

                        #for l in Reg.SpecialMsg.Order:
                        #    if(_order == l[1]):
                        #        _reply = Msg.GroupHandler.onOrderMsg(self,_group,_qq,_order)
                        #        if(not(_reply)):
                        #            self.api.send_group_msg(_group,Game.Config.CommenReply)
                        #            return
                        #        self.api.send_group_msg(_group,_reply)
                        #        return
                        
                        for l in Reg.SpecialMsg.Favor:
                            if(_order == l[1]):
                                Sql.User.addFavor(None,_group,_qq,1)
                                _reply = Msg.GroupHandler.onFavorMsg(self,_group,_qq,_order)
                                if(not(_reply)):
                                    self.api.send_group_msg(_group,Game.Config.CommenReply)
                                    return
                                self.api.send_group_msg(_group,_reply)
                                return
                        _reply = Msg.GroupHandler.onOrderMsg(self,_group,_qq,_order)
                        if(not _reply):
                            _reply = Msg.GroupHandler.onNormalMsg(self,_group,_qq,_order)
                            if(not _reply): return
                        self.api.send_group_msg(_group,_reply)
                        return
            return