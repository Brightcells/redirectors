# -*- coding: utf-8 -*-

import hashlib
import urllib


class Redirector(object):
    def egret(self, chanId=None, appKey=None, login_url=None, userid=None, username=None, avatar=None, sex=None):
        sign_str = 'chanId={chanId}&userid={userid}&{appKey}'.format(
            chanId=chanId,
            userid=userid,
            appKey=appKey
        )
        sign = hashlib.md5(sign_str).hexdigest()
        params = {
            'userid': userid,
            'username': username,
            'avatar': avatar,
            'sex': sex,
            'chanId': chanId,
            'sign': sign
        }
        return '{login_url}?{params}'.format(login_url=login_url, params=urllib.urlencode(params))


_global_instance = Redirector()
egret = _global_instance.egret
compet = _global_instance.egret
