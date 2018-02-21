###parse user data to vcs

import json
import csv
import io

outputFile = open('output.csv', 'a')

outputWriter = csv.writer(outputFile)
#outputWriter.writerow([unicode('uid'), u'location', u'nickname', u'num_fans',u'num_follow',u'num_weibo',u'self-intro',u'url',u'verify_info'])

with open("user_data.txt") as f:
    for line in f:
        if (line != '\n'):
            string = line.rstrip()
            try:
                data = json.loads(string)
                print data['uid']
                print data['data']['location']
                print data['data']['nickname']
                print data['data']['num_fans']
                print data['data']['num_follow']
                print data['data']['num_weibo']
                print data['data']['self-intro']
                print data['data']['url']
                print data['data']['verify_info']

                outputWriter.writerow([data['uid'],
                                       unicode(data['data']['location']).encode('utf-8'),
                                       unicode(data['data']['nickname']).encode('utf-8'),
                                       unicode(data['data']['num_fans']).encode('utf-8'),
                                       unicode(data['data']['num_follow']).encode('utf-8'),
                                       unicode(data['data']['num_weibo']).encode('utf-8'),
                                       unicode(data['data']['self-intro']).encode('utf-8'),
                                       unicode(data['data']['url']).encode('utf-8'),
                                       unicode(data['data']['verify_info']).encode('utf-8'),
                                       ])
            except ValueError:
                continue


            #outputWriter.writerow([(data['uid'])])

outputFile.close()

#data['data']['num_fans'], data['data']['num_follow'], data['data']['num_weibo'],
#, data['data']['nickname'], data['data']['self-intro'], data['data']['url'], data['data']['verify_info']
#, data['data']['location']
