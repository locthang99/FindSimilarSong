import json
import os,sys
import math
from re import T
import librosa
import threading

import librosa
from tqdm import tqdm
import numpy as np
from python_speech_features import mfcc, fbank, logfbank
import json
from annoy import AnnoyIndex


GENRE = "nhactre"
FOL_WAV = r"DATA"
FOL_OUT_MFCC = r"MFCC"

AUDIO_PER_FILE = 25

if not os.path.exists(FOL_OUT_MFCC):
    os.mkdir(FOL_OUT_MFCC)

SAMPLE_RATE = 22050
TRACK_DURATION = 30 # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION


def save_mfcc(LAST_HIT,MIN_INDEX_FILE,MAX_INDEX_FILE):
    data = {     
        "mfcc": []
    }
    songs = {"data":[]}
    print(str(MIN_INDEX_FILE))
    total_audio = 0
    for f in os.listdir(FOL_WAV):
    # load audio file
        if total_audio >= MIN_INDEX_FILE*AUDIO_PER_FILE and total_audio < MAX_INDEX_FILE*AUDIO_PER_FILE:
            try:
                file_path = os.path.join(FOL_WAV, f)

                y, sr = librosa.load(file_path, sr=16000)
                feat = extract_features(y)
                for i in range(0, feat.shape[0] - 10, 5):
                    data['mfcc'].append(crop_feature(feat, i, nb_step=10))
                    songs['data'].append(f)
            except:
                print("Error")

            if total_audio%AUDIO_PER_FILE==AUDIO_PER_FILE-1:
                print("Dump file :"+str(index_file))
                with open(FOL_OUT_MFCC+"/"+GENRE+str(index_file)+".json", "w+") as fp:
                    json.dump(data, fp, indent=4)
                index_file +=1
                data = {
                    "mfcc": []
                }
        total_audio +=1
    if LAST_HIT==True:
        print("Dump file :"+str(index_file))
        with open(FOL_OUT_MFCC+"/"+GENRE+str(index_file)+".json", "w+") as fp:
            json.dump(data, fp, indent=4)
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

if __name__ == "__main__":
    print(GENRE)
    threads = 4
    t1 = threading.Thread(target=save_mfcc,args=(False,0,1))
    t2 = threading.Thread(target=save_mfcc,args=(False,1,2))
    t3 = threading.Thread(target=save_mfcc,args=(False,2,3))
    t4 = threading.Thread(target=save_mfcc,args=(False,3,4))


    jobs = []

    jobs.append(t1)
    jobs.append(t2)
    jobs.append(t3)
    jobs.append(t4)
    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()
    #save_mfcc(MIN_INDEX_FILE=6,MAX_INDEX_FILE=8,num_segments=10,)
