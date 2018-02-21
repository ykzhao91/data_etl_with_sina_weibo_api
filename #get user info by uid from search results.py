#get user info by uid from search results

from weibo import APIClient
import json
APP_KEY = '4169394332' # app key
APP_SECRET = 'af941725411e192c803c439070acaf15' # app secret
CALLBACK_URL = 'https://github.com/ming-body7' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

access_token = '2.00FdFMgCgv2KYEa8ba2c3faa0vNP8U'
expires_in = '157679999'

client.set_access_token(access_token, expires_in)

queue = []
with open("title_uid_dataset.txt") as f:
    for line in f:
        if (line != '\n'):
            string = line.rstrip()
            # print string
            title = string.split(' ')[0].split(':')[1]
            uid = string.split(' ')[1].split(':')[1]
            queue.append(uid)

visited = set()

with io.open('user_data.txt', 'a', encoding='utf8') as outfile:
    for uid in queue:
        if uid in visited:
            continue
        json_data = client.search.users(uid)
        user_data = {
            'uid':url.split('/')[3],
            'data':json_data
        }
        visited.add(url)
        data = json.dumps(user_data, ensure_ascii=False)
        outfile.write(unicode(data))
        outfile.write(u"\n")