import json

with open('Metadata_Records') as json_file:
    metadata = json.load(json_file)

with open('SAWS_Climate_Change_Atlas_2036_2065.txt') as json_file:
    atlas = json.load(json_file)

#Metadata Keys
M_keys=[]
for y in range(len(metadata['children'][0]['children'])):
    M_keys.append(metadata['children'][0]['children'][y]['jsonData']['additionalFields']['onlineResources'][1]['href'])

for y in range(len(atlas["body"]["items"])):
    for x in xrange(len(atlas["body"]["items"][y]["layers"])):
        try:
            rog = M_keys.index(atlas["body"]["items"][y]["layers"][x]['dataAccessURL'])
            atlas["body"]["items"][y]["layers"][x]['guid'] = metadata['children'][0]['children'][rog]['uid']
            atlas["body"]["items"][y]["layers"][x]['link'] = metadata['children'][0]['children'][rog]['context_path']
        except:
            print(atlas["body"]["items"][y]["layers"][x]['title'])

j = json.dumps(atlas, indent=2)
f = open('SAWS_CC_ATLAS_2065.json', 'w')
print >> f, j
f.close()