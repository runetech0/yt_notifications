import xml.etree.ElementTree as XML

feed = '''<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015" xmlns="http://www.w3.org/2005/Atom"><link rel="hub" href="https://pubsubhubbub.appspot.com"/><link rel="self" href="https://www.youtube.com/xml/feeds/videos.xml?channel_id=UCUBJbdy8sL5gfjkzHilWCrQ"/><title>YouTube video feed</title><updated>2021-02-05T05:28:28.647444806+00:00</updated><entry>
  <id>yt:video:ByCHqXkJ-pU</id>
  <yt:videoId>ByCHqXkJ-pU</yt:videoId>
  <yt:channelId>UCUBJbdy8sL5gfjkzHilWCrQ</yt:channelId>
  <title>Test an upload</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=ByCHqXkJ-pU"/>
  <author>
   <name>Rehman Ali</name>
   <uri>https://www.youtube.com/channel/UCUBJbdy8sL5gfjkzHilWCrQ</uri>
  </author>
  <published>2021-02-05T05:28:10+00:00</published>
  <updated>2021-02-05T05:28:28.647444806+00:00</updated>
 </entry></feed>
'''

namespaces = {
    'yt': 'http://www.youtube.com/xml/schemas/2015',
    'xmlns': 'http://www.w3.org/2005/Atom'
}
root = XML.fromstring(feed)
for entry in root.findall('xmlns:entry', namespaces=namespaces):
    deleted = entry.find('at:deleted-entry')
    if deleted:
        # return
        pass
    video_id = entry.find('yt:videoId', namespaces=namespaces).text
    title = entry.find('xmlns:title', namespaces=namespaces).text
    link = entry.find('xmlns:link', namespaces=namespaces).get('href')
    for el in entry.find(
            'xmlns:author', namespaces=namespaces):
        if el.tag.split('}')[-1] == 'name':
            author = el.text

    message = f'{author} just posted a video on youtube!\nCheck this out {link}'
