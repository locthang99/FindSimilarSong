import re
import os
import json
# with open("DATA_LYRIC/10001.txt", "r",encoding='utf-8') as fp:
#     song = fp.read()

def remove_sign(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s

lyrics = {'data':[]}
for file in os.listdir("DATA_LYRIC"):
    print(file)
    data =''
    full_path = os.path.join('DATA_LYRIC', file)
    with open(full_path, "r",encoding='utf-8') as fp:
        song = fp.read()
    data = re.sub(r'\[.*\]','',song)
    data = re.sub(r'\n',' ',data)
    data = re.sub(r' +',' ',data)
    data = remove_sign(data)
    data=data.lower()
    lyrics['data'].append({'id':int(file.replace('.txt','')),'lyric':data})
    
# print(data)
# print(data.find("đời em ơi mấy đời em ơi mấy đời em thương"))
with open("lyric_all.json", "w+",encoding='utf-8') as fp:
        json.dump(lyrics, fp, indent=2,ensure_ascii=False)