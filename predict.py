import os
import glob
import librosa
from tqdm import tqdm
import numpy as np
from python_speech_features import mfcc, fbank, logfbank
import json
from annoy import AnnoyIndex
from collections import Counter
import os,sys

def extract_features(y, sr=16000, nfilt=10, winsteps=0.02):
    try:
        feat = mfcc(y, sr, nfilt=nfilt, winstep=winsteps)
        return feat
    except:
        print("Extraction feature error")

def crop_feature(feat, i = 0, nb_step=10, maxlen=100):
    sys.stdout = open(os.devnull, 'w')
    crop_feat = np.array(feat[i : i + nb_step]).flatten()
    print(crop_feat.shape)
    crop_feat = np.pad(crop_feat, (0, maxlen - len(crop_feat)), mode='constant')
    sys.stdout = sys.__stdout__
    return crop_feat

sys.stdout = open(os.devnull, 'w')
#y, sr = librosa.load("songgiocut.mp3", sr=16000)
y, sr = librosa.load("Recording (7).m4a", sr=16000)
#y, sr = librosa.load("DATA_VPOP/10118.mp3", sr=16000)
sys.stdout = sys.__stdout__
feat = extract_features(y)


u = AnnoyIndex(100,metric='angular')
u.load('RESULT/model_nhactre.ann')
with open("RESULT/mapping_nhactre.json", "r") as fp:
    songs = json.load(fp)
results = []
for i in range(0, feat.shape[0], 10):
    crop_feat = crop_feature(feat, i, nb_step=10)
    result = u.get_nns_by_vector(crop_feat, n=300)
    result_songs = [songs['data'][k] for k in result]
    results.append(result_songs)
    
results = np.array(results).flatten()

print("result:")
most_song = Counter(results)
print(most_song.most_common(100))


