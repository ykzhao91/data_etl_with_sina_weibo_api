###search user info using keyword 'wedding'

import json
APP_KEY = '4169394332' # app key
APP_SECRET = 'af941725411e192c803c439070acaf15' # app secret
CALLBACK_URL = 'https://github.com/ming-body7' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

access_token = '2.00FdFMgCgv2KYEa8ba2c3faa0vNP8U'
expires_in = '157679999'

client.set_access_token(access_token, expires_in)
raw_data = client.search.suggestion.users(q='wedding')
uid_list = raw_data.results.data.uids
file = open('uid','w')
file.write(json.dumps(uid_list))
file.close()