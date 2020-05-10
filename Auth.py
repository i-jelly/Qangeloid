# -*- coding:utf-8 -*-
import Sql
import Game

def AuthNorUser(func):
    def wrapper(group,qq,msg):
        
        if(Sql.User.isExists(None,group,qq)):
            if(Sql.User.getAuthLevel(None,group,qq) >= Game.Config.NorUserLevel):
                return func(group,qq,msg)
            return False
        return False
    return wrapper

def AuthUserFavorLevel(func):
    def wrapper(group,qq,msg,level):
        if(Sql.User.isExists(None,group,qq)):
            _level = Sql.User.getFavor(None,group,qq)
            if(_level >= Game.Config.HigFavorLevelThres):
                return func(group,qq,msg,4)
            elif(_level >= Game.Config.MidFavorLevelThres):
                return func(group,qq,msg,3)
            elif(_level >= Game.Config.LowFavorLevelThres):
                return func(group,qq,msg,2)
            return func(group,qq,msg,1)
        return False
    return wrapper

def AuthPremiumUser(func):
    def wrapper(group,qq,msg):
        if(Sql.User.isExists(None,group,qq)):
            if(Sql.User.getAuthLevel(None,group,qq) >= Game.Config.PremiumUserLevel):
                return func(group,qq,msg)
            return False
        return False
    return wrapper
    
def AuthAdminUser(func):
    def wrapper(group,qq,msg):
        if(Sql.User.isExists(None,group,qq)):
            if(Sql.User.getAuthLevel(None,group,qq) >= Game.Config.AdminUserLevel or str(qq) in Game.Config.Admin):
                return func(group,qq,msg)
            return False
        return False
    return wrapper

def AuthHighFavorLevel(func):
    def wrapper(group,qq,msg):
        if(Sql.User.isExists(None,group,qq)):
            if(Sql.User.getFavor(None,group,qq) >= Game.Config.HigFavorLevelThres):
                return func(group,qq,msg)
            return False
        return False
    return wrapper

def AuthMidFavorLevel(func):
    def wrapper(group,qq,msg):
        if(Sql.User.isExists(None,group,qq)):
            if(Sql.User.getFavor(None,group,qq) >= Game.Config.MidFavorLevelThres):
                return func(group,qq,msg)
            return False
        return False
    return wrapper
    
def AuthLowFavorLevel(func):
    def wrapper(group,qq,msg):
        if(Sql.User.isExists(None,group,qq)):
            if(Sql.User.getFavor(None,group,qq) >= Game.Config.LowFavorLevelThres):
                return func(group,qq,msg)
            return False
        return False
    return wrapper