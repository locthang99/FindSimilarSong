import os,sys
import glob
import librosa
from tqdm import tqdm
import numpy as np
from python_speech_features import mfcc, fbank, logfbank
import json
from annoy import AnnoyIndex

def extract_features(y, sr=16000, nfilt=10, winsteps=0.02):
    try:
        feat = mfcc(y, sr, nfilt=nfilt, winstep=winsteps)
        return feat
    except:
        raise Exception("Extraction feature error")

def crop_feature(feat, i = 0, nb_step=10, maxlen=100):
    sys.stdout = open(os.devnull, 'w')
    crop_feat = np.array(feat[i : i + nb_step]).flatten()
    print(crop_feat.shape)
    crop_feat = np.pad(crop_feat, (0, maxlen - len(crop_feat)), mode='constant')
    sys.stdout = sys.__stdout__
    return crop_feat



INPUT = "DATA_CACHMANG"
songs ={"data":[]}
features= {"data":[]}
for song in tqdm(os.listdir(INPUT)):
    print(song)
    full_path = os.path.join(INPUT, song)
    y, sr = librosa.load(full_path, sr=16000)
    feat = extract_features(y)
    for i in range(0, feat.shape[0] - 10, 5):
        features['data'].append(crop_feature(feat, i, nb_step=10).tolist())
        songs['data'].append(song)
with open("RESULT/mfcc_cachmang.json", "w+") as fp:
        json.dump(features, fp, indent=2)
with open("RESULT/mapping_cachmang.json", "w+") as fp:
        json.dump(songs, fp, indent=2)


f = 100
t = AnnoyIndex(f)
for i in range(len(features['data'])):
    v = features['data'][i]
    t.add_item(i, v)
t.build(100) # 100 trees
t.save('RESULT/model_cachmang.ann')