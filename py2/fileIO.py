#テキストファイル
f = open("sample.txt", "r", encoding="utf-8")
contents = f.read()
for content in contents:
    print(content, end="")
f.close()