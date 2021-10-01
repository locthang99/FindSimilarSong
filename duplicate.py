import json
import requests
with open("JSON_SONG/nhactre.json", "r",encoding='utf-8') as fp:
    songs = json.load(fp)

with open("JSON_SONG/vpop.json", "r",encoding='utf-8') as fp:
    songs2 = json.load(fp)

for song2 in songs2['data']:
    flg = 0
    for song in songs['data']:
        if song['name'] == song2['name']:
            flg = 1
        if song['id'] == 10099 and flg==0:
            print(song2['id'])
            # r = requests.get(song2['fileMusic128'])
            # open("DATA_VPOP/"+str(song2['id'])+".mp3",'wb').write(r.content)
