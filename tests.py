import json

config = json.load(open('config.json', 'r'))

desc = config.get("DESCRIPTION")

desc = desc.replace('VIDEO_LINK_HERE', 'https://youtube.com')
print(desc)
