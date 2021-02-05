from bottle import route, run, request, default_app, abort, app
import xml.etree.ElementTree as XML

secret = 'some_url_safe_secret'

namespaces = {
    'yt': 'http://www.youtube.com/xml/schemas/2015',
    'xmlns': 'http://www.w3.org/2005/Atom'
}


@route('/callback', method='get')
@route('/callback', method='post')
def index():
    if request.method == 'POST':
        response = request.body.read().decode('utf-8')
        root = XML.fromstring(response)

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
            print(message)

        # Do Something Here

        return 'Goodly'

    try:
        mode = request.query['hub.mode']
        challenge = request.query['hub.challenge']
        return challenge
        verify_token = request.query['hub.verify_token']
    except KeyError:
        print('KeyError, Aborting ..')
        abort(404)

    if mode == 'subscribe' and verify_token == secret:
        return challenge
    abort(404)


if __name__ == '__main__':
    """For Development"""
    run(host='0.0.0.0', port=80, debug=True)

# For Production
app = app()
