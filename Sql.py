# -*- coding:utf-8 -*-

import sqlite3
import time
import Game

class Base:
    def __init__(self):
        super().__init__()

    def executeSQL(self,group,stat):
        _conn = sqlite3.connect(str(group) + "db")
        _c = _conn.cursor()
        try:
            _c.execute(stat)
            _conn.commit()
            _res = _c.fetchall()
            _conn.close()
            return _res
        except:
            _conn.close()
            return False
    
    def hasTable(self,group,table):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _res = _c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name = '{}'".format(table))
        if(_res.fetchone()[0] >= 1):
            _conn.close()
            return True
        else:
            _conn.close()
            return False

    def initTable(self,group):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("CREATE TABLE User (\
                    id INTEGER PRIMARY  KEY     AUTOINCREMENT,\
                    QQ                  TEXT    NOT NULL,\
                    Cash                TEXT    NOT NULL,\
                    JoinDate            INT     NOT NULL,\
                    LastSign            INT     NOT NULL,\
                    LastS               INT     NOT NULL,\
                    LastSS              INT     NOT NULL,\
                    AuthLevel           INT     NOT NULL,\
                    Favor               INT     NOT NULL,\
                    Call                TEXT    DEFAULT 'ご主人',\
                    Called              TEXT    DEFAULT '小丛雨'\
            )")
        _conn.commit()
        _c.execute("CREATE TABLE Ava (\
                    id INTEGER PRIMARY  KEY     AUTOINCREMENT,\
                    QQ                  TEXT    NOT NULL,\
                    Ava                 TEXT    NOT NULL,\
                    Type                TEXT    NOT NULL\
            )")
        _conn.commit()
        _c.execute("CREATE TABLE LotHis (\
                    id INTEGER PRIMARY  KEY     AUTOINCREMENT,\
                    QQ                  TEXT    NOT NULL,\
                    Ava                 TEXT    NOT NULL,\
                    Type                TEXT    NOT NULL\
            )")
        _conn.commit()
        _conn.close()
        return True

class User:

    def __init__(self):
        super().__init__()

    def setCall(self,group,qq,msg):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("UPDATE User SET Call = '{}' WHERE QQ = '{}'".format(msg,qq))
        _conn.commit()
        _conn.close()
        return True

    def setCalled(self,group,qq,msg):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("UPDATE User SET Called = '{}' WHERE QQ = '{}'".format(msg,qq))
        _conn.commit()
        _conn.close()
        return True

    def getCall(self,group,qq):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT Call FROM User WHERE QQ = '{}'".format(qq))
        _res = _c.fetchone()[0]
        _conn.close()
        return _res
    
    def getCalled(self,group,qq):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT Called FROM User WHERE QQ = '{}'".format(qq))
        _res = _c.fetchone()[0]
        _conn.close()
        return _res

    def addUser(self,group,qq):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        try:
            _c.execute("INSERT INTO User (QQ,Cash,JoinDate,LastSign,LastS,LastSS,AuthLevel,Favor) VALUES ('{}','{}',{},{},{},{},{},{})".format(qq,5000,int(time.time()) + 28800,0,Game.Config.GuaranS,Game.Config.GuaranSS,Game.Config.NorUserLevel,0))
            _conn.commit()
            _conn.close()
            return True
        except:
            _conn.close()
            return False

    def isExists(self,group,qq):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT COUNT(*) FROM User WHERE QQ = '{}'".format(qq))
        if(_c.fetchone()[0] >= 1):
            _conn.close()
            return True
        else:
            _conn.close()
            return False

    def getCards(self,group,qq,atype):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        li = []
        _c.execute("SELECT Ava FROM Ava WHERE QQ = '{}' AND Type = '{}'".format(qq,atype))
        res = _c.fetchall()
        for i in res:
            li.append(i[0])
        return li

    def getCash(self,group,qq):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT Cash FROM User WHERE QQ = '{}'".format(qq))
        _res = _c.fetchone()[0]
        _conn.close()
        return _res
    
    def setCash(self,group,qq,num):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("UPDATE User SET Cash = '{}' WHERE QQ = '{}'".format(num,qq))
        _conn.commit()
        _conn.close()
        return True


    def renewSign(self,group,qq):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _now = time.localtime(time.time())[0] * 1000 + time.localtime(time.time())[1] * 100 + time.localtime(time.time())[2]
        _c.execute("SELECT LastSign FROM User WHERE QQ = '{}'".format(qq))
        _reco = int(_c.fetchone()[0])
        if(_now > _reco):
            _c.execute("UPDATE User SET LastSign = {} WHERE QQ = '{}'".format(_now,qq))
            _conn.commit()
            _conn.close()
            return True
        else:
            _conn.close()
            return False
    
    def hasAva(self,group,qq,atype,ava):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT COUNT(*) FROM Ava WHERE QQ = '{}' AND Ava = '{}' AND Type = '{}'".format(qq,atype,ava))
        if(_c.fetchone()[0] > 0):
            _conn.close()
            return True
        else:
            _conn.close()
            return False
    
    def addAva(self,group,qq,atype,ava):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        try:
            _c.execute("INSERT INTO Ava (QQ,Ava,Type) VALUES ('{}','{}','{}')".format(qq,ava,atype))
            _conn.commit()
            _conn.close()
        except:
            _conn.close()
            return False
        return True

    def addHis(self,group,qq,atype,ava):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        try:
            _c.execute("INSERT INTO LotHis (QQ,Ava,Type) VALUES ('{}','{}','{}')".format(qq,ava,atype))
            _conn.commit()
            _conn.close()
        except:
            _conn.close()
            return False
        return True

    def getAuthLevel(self,group,qq):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT AuthLevel FROM User WHERE QQ = '{}'".format(qq))
        _res = _c.fetchone()[0]
        _conn.close()
        return _res

    def setAuthLevel(self,group,qq,level):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("UPDATE User SET AuthLevel = {} WHERE QQ = '{}'".format(level,qq))
        _conn.commit()
        _conn.close()
        return True

    def addFavor(self,group,qq,num):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        try:
            _c.execute("SELECT Favor FROM User WHERE QQ = '{}'".format(qq))
            _res = int(_c.fetchone()[0]) + num
            _c.execute("UPDATE User SET Favor = {} WHERE QQ = '{}'".format(_res,qq))
        except:
            return
        _conn.commit()
        _conn.close()
        return True
    
    def getFavor(self,group,qq):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT Favor FROM User WHERE QQ = '{}'".format(qq))
        _res = _c.fetchone()[0]
        _conn.close()
        return _res
    
    def setLastS(self,group,qq,num):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT LastS FROM User WHERE QQ = '{}'".format(qq))
        _res = _c.fetchone()[0]
        if(num == 0):
            _conn.close()
            return _res
        elif(num == 1):
            _c.execute("UPDATE User SET LastS = {}".format(_res - 1))
            _conn.commit()
            _conn.close()
            return _res - 1
        elif(num == -1):
            _c.execute("UPDATE User SET LastS = {}".format(Game.Config.GuaranS))
            _conn.commit()
            _conn.close()
            return True
        else:
            return False

    def setLastSS(self,group,qq,num):
        _conn = sqlite3.connect(str(group) + ".db")
        _c = _conn.cursor()
        _c.execute("SELECT LastSS FROM User WHERE QQ = '{}'".format(qq))
        _res = _c.fetchone()[0]
        if(num == 0):
            _conn.close()
            return _res
        elif(num == 1):
            _c.execute("UPDATE User SET LastSS = {}".format(_res - 1))
            _conn.commit()
            _conn.close()
            return _res - 1
        elif(num == -1):
            _c.execute("UPDATE User SET LastSS = {}".format(Game.Config.GuaranSS))
            _conn.commit()
            _conn.close()
            return True
        else:
            return False