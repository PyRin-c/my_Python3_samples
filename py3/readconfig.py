#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# コンフィグ読み込み用モジュール
import configparser

# ファイルがあるかの確認用モジュール
import os
import errno

def make_config():
    config = configparser.ConfigParser()

    config['CONFIG1'] = {
        'data1': '1111111',
        'data2': '2222222'
    }
    config['CONFIG2'] = {
        'string': 'abcdefg',
        'number': 123456789,
        'bool': False
    }

    with open('config.ini', 'w', encoding='utf-8') as file:
        config.write(file)

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

    print(config['CONFIG1']['data1'])
    print(config['CONFIG2']['number'])

def configsettings():
    config = configparser.ConfigParser()
    config_path = 'config.ini'

    # 指定したiniファイルが存在しない場合、エラー発生
    if not os.path.exists(config_path):
        make_config()
        # raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_path)

    config.read(config_path, encoding='utf-8')

    print(config['CONFIG1']['data1'])
    print(config['CONFIG2']['number'])

if __name__ == "__main__":
    # make_config()
    # read_config()
    configsettings()