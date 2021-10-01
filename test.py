import os
for song in os.listdir("DATA_DANCA"):
    full_path = os.path.join("DATA_DANCA", song)
    if os.path.getsize(full_path) <500:
        print(song)