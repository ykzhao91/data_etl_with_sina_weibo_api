###get top 100 user weibo


    from weibo import APIClient
    import json
    APP_KEY = '4169394332' # app key
    APP_SECRET = 'af941725411e192c803c439070acaf15' # app secret
    CALLBACK_URL = 'https://github.com/ming-body7' # callback url

    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    # TODO: redirect to url

    access_token = '2.00FdFMgCgv2KYEa8ba2c3faa0vNP8U'
    expires_in = '157679999'


    queue = []
    with open("top_50.txt") as f:
        for line in f:
            if (line != '\n'):
                string = line.rstrip()
                uid = line.rstrip()
                url = 'http://weibo.cn/'+uid
                queue.append(uid)

    json_data = client.users.show.get(uid=queue[0])
    print json_data

    visited = set()

    with io.open('top_50_results.txt', 'a', encoding='utf8') as outfile:
        for uid in queue:
            if uid in visited:
                continue
            json_data = cclient.users.weibo.get(uid)
            user_data = {
                'uid':uid,
                'data':json_data
            }
            visited.add(url)
            data = json.dumps(user_data, ensure_ascii=False)
            outfile.write(unicode(data))
            outfile.write(u"\n")