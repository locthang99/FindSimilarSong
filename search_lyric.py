import json
with open("lyric_all.json", "r",encoding='utf-8') as fp:
    lyrics = json.load(fp)


key = "ai mang co don di"

for lyric in lyrics['data']:
    if lyric['lyric'].find(key) > -1:
        print(lyric['id'])
