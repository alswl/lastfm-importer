# lastfm importer

## What

Lastfm importer can import music to lastfm love tracks from local disk.

Lastfm importer 可以将本地音乐文件提交到 Last.fm 的喜爱曲目中。

## Requires

Python 2.x

I only test in Linux!

我在Linux中使用无误，如果Windows上面有问题，欢迎报告bug。

## Install

	cd lastfm-importer
	./setup install # install the requires / 安装必须的依赖

## Useage

    ~/dev/myproject/python/lastfm-importer/app.py ./AI
    ~/dev/myproject/python/lastfm-importer/app.py ./AI ./AB/

The AI and AB is folder names.

AI 和 AB 是音乐目录的名称，lastfm importer 会将所有子目录中音乐导入。
