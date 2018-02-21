####parse top 100 weibo into cvs

import json
import csv
import io

outputFile = open('output_top100.csv', 'a')

outputWriter = csv.writer(outputFile)
#outputWriter.writerow([unicode('uid'), u'location', u'nickname', u'num_fans',u'num_follow',u'num_weibo',u'self-intro',u'url',u'verify_info'])

with open("top_50_results.txt") as f:
    for line in f:
        if (line != '\n'):
            string = line.rstrip()
            try:
                data = json.loads(string)
                print data['uid']

                for weibo in data['data']['weibo']:

                    try:
                        print weibo['comment'].split('[')[1].split(']')[0]
                        print weibo['pic']
                        print weibo['repost'].split('[')[1].split(']')[0]
                        print weibo['like'].split('[')[1].split(']')[0]
                        print weibo['type']

                        outputWriter.writerow([data['uid'],
                                               unicode(weibo['type']).encode('utf-8'),
                                               unicode(weibo['like'].split('[')[1].split(']')[0]).encode('utf-8'),
                                               unicode(weibo['comment'].split('[')[1].split(']')[0]).encode('utf-8'),
                                               unicode(weibo['repost'].split('[')[1].split(']')[0]).encode('utf-8'),
                                               unicode(weibo['pic']).encode('utf-8'),
                                               ])
                    except IndexError:
                        continue
            except ValueError:
                continue




outputFile.close()
