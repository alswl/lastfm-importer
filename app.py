#!/usr/bin/env python
#coding=utf-8

# desc: 将本地音乐文件添加到last.fm的喜爱曲目中
# author: alswl<http://log4d.com>
# date: 2012-03-14

import sys
import os
sys.path.append(os.path.abspath('./lib/lastfm-0.2-py2.7.egg'))
import webbrowser
import yaml
import argparse

import lastfm

reload(sys) # fix encode error
sys.setdefaultencoding('utf-8')

def get_config():
    return yaml.load(file('./config.yaml','r'), yaml.Loader)

def save_session_key(session_key):
    """将session_key保存到本地"""
    config = get_config()
    config['keys']['session_key'] = session_key
    yaml.dump(config, file('./config.yaml','w'))

def get_api():
    """获取api"""
    config = get_config()
    API_Key = config['keys']['api_key']
    SECRET = config['keys']['secret']
    session_key = config['keys']['session_key']
    if session_key == '' or session_key is None:
        api = lastfm.Api(API_Key, SECRET)
        set_session_key(api)
        save_session_key(api.session_key)
    else:
        api = lastfm.Api(API_Key, SECRET, session_key)
    return api

def set_session_key(api):
    """设置session key"""
    webbrowser.open_new(api.auth_url)
    raw_input(u'请在打开的浏览器中授权，授权通过之后按<Enter>继续')
    api.set_session_key()
    return api.session_key

def love_music(api, filename):
    """喜欢音乐动作"""
    artist, title = map(lambda x: x.strip().replace('.mp3', ''),
                        filename.split('-'))
    track = api.get_track(title, artist)
    track.love()

def walk_love(api, path):
    """走爱"""
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            walk_love(api, dir)
        for file in files:
            try:
                love_music(api, file.decode('utf-8'))
                print '-> %s' %file
            except IndexError:
                print '-X %s' %file
                continue

def main():
    parser = argparse.ArgumentParser(
        )
    parser.add_argument('path',
                        metavar='Path',
                        type=str,
                        nargs='+',
                       )
    args = parser.parse_args()

    api = get_api()
    for path in args.path:
        walk_love(api, path)

if __name__ == '__main__':
    main()