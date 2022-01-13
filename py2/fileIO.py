#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#テキストファイル(.txt .csv)
f = open("sample.txt", "r", encoding="utf-8")
#part1
contents = f.read()
for content in contents:
    print(content, end="")
#f.close()

#part2
while True:
    data = f.readline()
    if data == '':
        break
    print(data)

f.close()