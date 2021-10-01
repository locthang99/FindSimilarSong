import json
import requests
with open("JSON_SONG/song_all.json", "r",encoding='utf-8') as fp:
    songs = json.load(fp)

for song in songs['data']:
    if (song['id']>10186 or song['id']==10118) and song['lyric']:
        print(song['id'])
        r = requests.get(song['lyric'])
        open("DATA_LYRIC/"+str(song['id'])+".txt",'wb').write(r.content)

