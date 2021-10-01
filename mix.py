import json
from annoy import AnnoyIndex
from collections import Counter

# print("loading")
# with open("RESULT/mfcc_final_300.json", "r") as fp:
#     mfcc = json.load(fp)
# print("load ok")
# print(str(len(mfcc['data'])))
# u = AnnoyIndex(100)
# for i in range(len(mfcc['data'])):
#     v = mfcc['data'][i]
#     u.add_item(i, v)
# u.build(100) # 100 trees
# u.save('RESULT/model_final_300.ann')


print("loading")
with open("RESULT/mfcc_nhactre.json", "r") as fp:
    mfcc1 = json.load(fp)

with open("RESULT/mfcc_vpop.json", "r") as fp:
    mfcc2 = json.load(fp)

mfcc = {'data':[]}
mfcc['data'] = mfcc1['data'] + mfcc2['data']
print("load ok")
l = len(mfcc['data'])
print(str(l))
u = AnnoyIndex(100)
for i in range(len(mfcc['data'])):
    v = mfcc['data'][i]
    u.add_item(i, v)
u.build(100) # 100 trees
u.save('RESULT/model_nhac_tre_vpop.ann')

########################################### MFCC
# with open("RESULT/mfcc_nhactre.json", "r") as fp:
#     mfcc1 = json.load(fp)

# with open("RESULT/mfcc_vpop.json", "r") as fp:
#     mfcc2 = json.load(fp)

# with open("RESULT/mfcc_cachmang.json", "r") as fp:
#     mfcc3 = json.load(fp)

# with open("RESULT/mfcc_nhactrinh.json", "r") as fp:
#     mfcc4 = json.load(fp)

# mfcc_all={'data':[]}
# mfcc_all['data'] += mfcc1['data']
# mfcc_all['data'] += mfcc2['data']
# mfcc_all['data'] += mfcc3['data']
# mfcc_all['data'] += mfcc4['data']

# with open("RESULT/mapping_final_300.json", "w+") as fp:
#     json.dump(mfcc_all, fp, indent=2)


#################################m MAPPING
with open("RESULT/mapping_nhactre.json", "r") as fp:
    mapping1 = json.load(fp)

with open("RESULT/mapping_vpop.json", "r") as fp:
    mapping2 = json.load(fp)

# with open("RESULT/mapping_cachmang.json", "r") as fp:
#     mapping3 = json.load(fp)

# with open("RESULT/mapping_nhactrinh.json", "r") as fp:
#     mapping4 = json.load(fp)

mapping_all={'data':[]}
mapping_all['data'] += mapping1['data']
mapping_all['data'] += mapping2['data']
# mapping_all['data'] += mapping3['data']
# mapping_all['data'] += mapping4['data']

with open("RESULT/mapping_nhac_tre_vpop.json", "w+") as fp:
    json.dump(mapping_all, fp, indent=2)