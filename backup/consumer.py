# import threading
# import logging
# import time
# import json

# from kafka import KafkaConsumer, KafkaProducer

# def main():
#     print "+++++++++++++++++++++++++++++++++++++++++++++++"
#     consumer = KafkaConsumer(bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))
#     consumer.subscribe(['my-topic'])

#     for message in consumer:
#         print (message)

# main()


import threading
import logging
import time
import json

from kafka import KafkaConsumer, KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        while True:
            producer.send('my-topic', [{"kg": {"a": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFF2C0F93A", "dateRecorded": "2017-08-10T10:10:24", "method": "karma"}], "value": "UserName", "key": "UserName"}], "publisher": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFF2C0F93A", "dateRecorded": "2017-08-10T10:10:24", "method": "karma"}], "value": "isi-twitter", "key": "isi-twitter"}], "name": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFF2C0F93A", "dateRecorded": "2017-08-10T10:10:24", "method": "karma"}], "value": "TT_Smolin", "key": "TT_Smolin"}], "source": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFF2C0F93A", "dateRecorded": "2017-08-10T10:10:24", "method": "karma"}], "value": "isi-twitter/FFFFFFFFF2C0F93A", "key": "isi-twitter/FFFFFFFFF2C0F93A"}]}, "timestamp_index": "2017-08-10T10:10:24Z", "raw_content": "", "timestamp_crawl": "2017-08-10T10:10:24Z", "_id": "http://effect.isi.edu/data/username/twitter/TT_Smolin", "doc_id": "http://effect.isi.edu/data/username/twitter/TT_Smolin"}, {"kg": {"username": [{"confidence": 1, "provenance": [{"source": "", "dateRecorded": "", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/username/twitter/LuisS923"}, "key": {"uri": "http://effect.isi.edu/data/username/twitter/LuisS923"}}], "a": [{"confidence": 1, "provenance": [{"source": "", "dateRecorded": "", "method": "karma"}], "value": "LoginCredentials", "key": "LoginCredentials"}]}, "_id": "http://effect.isi.edu/data/logincredentials/twitter/LuisS923", "doc_id": "http://effect.isi.edu/data/logincredentials/twitter/LuisS923", "raw_content": ""}, {"kg": {"a": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFB8263449", "dateRecorded": "2017-06-16T21:37:59", "method": "karma"}], "value": "Extraction", "key": "Extraction"}], "extractor": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFB8263449", "dateRecorded": "2017-06-16T21:37:59", "method": "karma"}], "value": "bbn-crfsuite", "key": "bbn-crfsuite"}], "publisher": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFB8263449", "dateRecorded": "2017-06-16T21:37:59", "method": "karma"}], "value": "isi-twitter", "key": "isi-twitter"}], "text": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFB8263449", "dateRecorded": "2017-06-16T21:37:59", "method": "karma"}], "value": "puppet\u2013Trump", "key": "puppet\u2013Trump"}], "hasType": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFB8263449", "dateRecorded": "2017-06-16T21:37:59", "method": "karma"}], "value": "HACKABLETHING", "key": "HACKABLETHING"}], "source": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFB8263449", "dateRecorded": "2017-06-16T21:37:59", "method": "karma"}], "value": "isi-twitter/FFFFFFFFB8263449", "key": "isi-twitter/FFFFFFFFB8263449"}]}, "timestamp_index": "2017-06-16T21:37:59Z", "raw_content": "", "timestamp_crawl": "2017-06-16T21:37:59Z", "_id": "http://effect.isi.edu/data/tweet/859200885972508672/extraction/HACKABLETHING/puppetTrump", "doc_id": "http://effect.isi.edu/data/tweet/859200885972508672/extraction/HACKABLETHING/puppetTrump"}, {"kg": {"a": [{"confidence": 1, "provenance": [{"source": "hg-blogs/14450FDF", "dateRecorded": "2017-08-14T19:50:06", "method": "karma"}], "value": "Extraction", "key": "Extraction"}], "extractor": [{"confidence": 1, "provenance": [{"source": "hg-blogs/14450FDF", "dateRecorded": "2017-08-14T19:50:06", "method": "karma"}], "value": "bbn-crfsuite", "key": "bbn-crfsuite"}], "publisher": [{"confidence": 1, "provenance": [{"source": "hg-blogs/14450FDF", "dateRecorded": "2017-08-14T19:50:06", "method": "karma"}], "value": "hg-blogs", "key": "hg-blogs"}], "text": [{"confidence": 1, "provenance": [{"source": "hg-blogs/14450FDF", "dateRecorded": "2017-08-14T19:50:06", "method": "karma"}], "value": "SQL injection", "key": "SQL injection"}], "hasType": [{"confidence": 1, "provenance": [{"source": "hg-blogs/14450FDF", "dateRecorded": "2017-08-14T19:50:06", "method": "karma"}], "value": "ATTACKTYPE", "key": "ATTACKTYPE"}], "source": [{"confidence": 1, "provenance": [{"source": "hg-blogs/14450FDF", "dateRecorded": "2017-08-14T19:50:06", "method": "karma"}], "value": "hg-blogs/14450FDF", "key": "hg-blogs/14450FDF"}]}, "timestamp_index": "2017-08-14T19:50:06Z", "raw_content": "", "timestamp_crawl": "2017-08-14T19:50:06Z", "_id": "http://effect.isi.edu/data/blogs/httpblogerrataseccom201308therobtest12stepstosafercodehtml/extraction/ATTACKTYPE/SQLinjection", "doc_id": "http://effect.isi.edu/data/blogs/httpblogerrataseccom201308therobtest12stepstosafercodehtml/extraction/ATTACKTYPE/SQLinjection"}, {"kg": {"a": [{"confidence": 1, "provenance": [{"source": "asu-hacking-posts/261EC260", "dateRecorded": "2017-08-04T14:00:43", "method": "karma"}], "value": "Topic", "key": "Topic"}], "hasPost": [{"confidence": 1, "provenance": [{"source": "asu-hacking-posts/261EC260", "dateRecorded": "2017-08-04T14:00:43", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/forum/266/topic/8835963E7EF09A08E8B252EEA0646ECBF49585CC/post/D543DA119C708F2BE1FD459136B0242581D70569"}, "key": {"uri": "http://effect.isi.edu/data/forum/266/topic/8835963E7EF09A08E8B252EEA0646ECBF49585CC/post/D543DA119C708F2BE1FD459136B0242581D70569"}}], "name": [{"confidence": 1, "provenance": [{"source": "asu-hacking-posts/261EC260", "dateRecorded": "2017-08-04T14:00:43", "method": "karma"}], "value": "67.197.29.243:27451|united states|south carolina|clover|29710|67-197-29-243.lw1.cm.dyn.comporium.net| 67.197.29.243 |time view 16/07/2017 16:19:03...", "key": "67.197.29.243:27451|united states|south carolina|clover|29710|67-197-29-243.lw1.cm.dyn.comporium.net| 67.197.29.243 |time view 16/07/2017 16:19:03..."}], "publisher": [{"confidence": 1, "provenance": [{"source": "asu-hacking-posts/261EC260", "dateRecorded": "2017-08-04T14:00:43", "method": "karma"}], "value": "asu-hacking-posts", "key": "asu-hacking-posts"}], "source": [{"confidence": 1, "provenance": [{"source": "asu-hacking-posts/261EC260", "dateRecorded": "2017-08-04T14:00:43", "method": "karma"}], "value": "asu-hacking-posts/261EC260", "key": "asu-hacking-posts/261EC260"}], "isTopicOf": [{"confidence": 1, "provenance": [{"source": "asu-hacking-posts/261EC260", "dateRecorded": "2017-08-04T14:00:43", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/forum/266"}, "key": {"uri": "http://effect.isi.edu/data/forum/266"}}]}, "timestamp_index": "2017-08-04T14:00:43Z", "raw_content": "", "timestamp_crawl": "2017-08-04T14:00:43Z", "_id": "http://effect.isi.edu/data/forum/266/topic/8835963E7EF09A08E8B252EEA0646ECBF49585CC", "doc_id": "http://effect.isi.edu/data/forum/266/topic/8835963E7EF09A08E8B252EEA0646ECBF49585CC"}, {"kg": {"a": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": "SocialMediaPosting", "key": "SocialMediaPosting"}], "publisher": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": "isi-twitter", "key": "isi-twitter"}], "repostCount": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": "0", "key": "0"}], "hasType": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": "Tweet", "key": "Tweet"}], "text": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": "Why Rockstar's Removal of A\u00a0GTA Online Car Exploit Is So Controversial\u00a0 https://t.co/DWh8ZwU6Ef", "key": "Why Rockstar's Removal of A\u00a0GTA Online Car Exploit Is So Controversial\u00a0 https://t.co/DWh8ZwU6Ef"}], "author": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/personOrOrganization/twitter/psizan"}, "key": {"uri": "http://effect.isi.edu/data/personOrOrganization/twitter/psizan"}}], "datePublished": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": "2017-01-30T22:23:36", "key": "2017-01-30T22:23:36"}], "source": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": "isi-twitter/1BFF1777", "key": "isi-twitter/1BFF1777"}], "favoriteCount": [{"confidence": 1, "provenance": [{"source": "isi-twitter/1BFF1777", "dateRecorded": "2017-07-15T06:07:51", "method": "karma"}], "value": "0", "key": "0"}]}, "timestamp_index": "2017-07-15T06:07:51Z", "raw_content": "", "timestamp_crawl": "2017-07-15T06:07:51Z", "_id": "http://effect.isi.edu/data/tweet/826194175997702144", "doc_id": "http://effect.isi.edu/data/tweet/826194175997702144"}, {"kg": {"a": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": "SocialMediaPosting", "key": "SocialMediaPosting"}], "publisher": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": "isi-twitter", "key": "isi-twitter"}], "repostCount": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": "0", "key": "0"}], "author": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/personOrOrganization/twitter/jw33062"}, "key": {"uri": "http://effect.isi.edu/data/personOrOrganization/twitter/jw33062"}}], "text": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": "RT @AriBerman: How democracy dies: \n Mass voter suppression \n Russian election hacking \n Stolen SCOTUS seat \n Voting on secret bills \n https://t\u2026", "key": "RT @AriBerman: How democracy dies: \n Mass voter suppression \n Russian election hacking \n Stolen SCOTUS seat \n Voting on secret bills \n https://t\u2026"}], "hasType": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": "Tweet", "key": "Tweet"}], "datePublished": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": "2017-07-28T02:56:39", "key": "2017-07-28T02:56:39"}], "mentionsPersonOrOrganization": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/personOrOrganization/AriBerman"}, "key": {"uri": "http://effect.isi.edu/data/personOrOrganization/AriBerman"}}], "source": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": "isi-twitter/7A8480FF", "key": "isi-twitter/7A8480FF"}], "favoriteCount": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": "0", "key": "0"}], "hasExtraction": [{"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/tweet/890767932485246978/extraction/HACKABLETHING/election"}, "key": {"uri": "http://effect.isi.edu/data/tweet/890767932485246978/extraction/HACKABLETHING/election"}}, {"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/tweet/890767932485246978/extraction/PERSON/hacking"}, "key": {"uri": "http://effect.isi.edu/data/tweet/890767932485246978/extraction/PERSON/hacking"}}, {"confidence": 1, "provenance": [{"source": "isi-twitter/7A8480FF", "dateRecorded": "2017-07-29T10:06:31", "method": "karma"}], "value": {"uri": "http://effect.isi.edu/data/tweet/890767932485246978/extraction/GPE/Russian"}, "key": {"uri": "http://effect.isi.edu/data/tweet/890767932485246978/extraction/GPE/Russian"}}]}, "timestamp_index": "2017-07-29T10:06:31Z", "raw_content": "", "timestamp_crawl": "2017-07-29T10:06:31Z", "_id": "http://effect.isi.edu/data/tweet/890767932485246978", "doc_id": "http://effect.isi.edu/data/tweet/890767932485246978"}, {"kg": {"a": [{"confidence": 1, "provenance": [{"source": "hg-blogs/FFFFFFFFA749AA68", "dateRecorded": "2017-08-14T20:31:08", "method": "karma"}], "value": "Extraction", "key": "Extraction"}], "extractor": [{"confidence": 1, "provenance": [{"source": "hg-blogs/FFFFFFFFA749AA68", "dateRecorded": "2017-08-14T20:31:08", "method": "karma"}], "value": "bbn-crfsuite", "key": "bbn-crfsuite"}], "publisher": [{"confidence": 1, "provenance": [{"source": "hg-blogs/FFFFFFFFA749AA68", "dateRecorded": "2017-08-14T20:31:08", "method": "karma"}], "value": "hg-blogs", "key": "hg-blogs"}], "text": [{"confidence": 1, "provenance": [{"source": "hg-blogs/FFFFFFFFA749AA68", "dateRecorded": "2017-08-14T20:31:08", "method": "karma"}], "value": "Applications", "key": "Applications"}], "hasType": [{"confidence": 1, "provenance": [{"source": "hg-blogs/FFFFFFFFA749AA68", "dateRecorded": "2017-08-14T20:31:08", "method": "karma"}], "value": "HACKABLETHING_DESC", "key": "HACKABLETHING_DESC"}], "source": [{"confidence": 1, "provenance": [{"source": "hg-blogs/FFFFFFFFA749AA68", "dateRecorded": "2017-08-14T20:31:08", "method": "karma"}], "value": "hg-blogs/FFFFFFFFA749AA68", "key": "hg-blogs/FFFFFFFFA749AA68"}]}, "timestamp_index": "2017-08-14T20:31:08Z", "raw_content": "", "timestamp_crawl": "2017-08-14T20:31:08Z", "_id": "http://effect.isi.edu/data/blogs/httpswwwwhitehatseccombloghackerkast38pulsetestsgovsiteschinahackedusgovernmentduckduckgonsaquantuminsertattacksandgooglefindsadblockingannoying/extraction/HACKABLETHING_DESC/Applications", "doc_id": "http://effect.isi.edu/data/blogs/httpswwwwhitehatseccombloghackerkast38pulsetestsgovsiteschinahackedusgovernmentduckduckgonsaquantuminsertattacksandgooglefindsadblockingannoying/extraction/HACKABLETHING_DESC/Applications"}, {"kg": {"a": [{"confidence": 1, "provenance": [{"source": "isi-twitter/44378B9D", "dateRecorded": "2017-06-15T07:21:46", "method": "karma"}], "value": "Extraction", "key": "Extraction"}], "extractor": [{"confidence": 1, "provenance": [{"source": "isi-twitter/44378B9D", "dateRecorded": "2017-06-15T07:21:46", "method": "karma"}], "value": "bbn-crfsuite", "key": "bbn-crfsuite"}], "publisher": [{"confidence": 1, "provenance": [{"source": "isi-twitter/44378B9D", "dateRecorded": "2017-06-15T07:21:46", "method": "karma"}], "value": "isi-twitter", "key": "isi-twitter"}], "text": [{"confidence": 1, "provenance": [{"source": "isi-twitter/44378B9D", "dateRecorded": "2017-06-15T07:21:46", "method": "karma"}], "value": "FINALLY", "key": "FINALLY"}], "hasType": [{"confidence": 1, "provenance": [{"source": "isi-twitter/44378B9D", "dateRecorded": "2017-06-15T07:21:46", "method": "karma"}], "value": "HACKABLETHING", "key": "HACKABLETHING"}], "source": [{"confidence": 1, "provenance": [{"source": "isi-twitter/44378B9D", "dateRecorded": "2017-06-15T07:21:46", "method": "karma"}], "value": "isi-twitter/44378B9D", "key": "isi-twitter/44378B9D"}]}, "timestamp_index": "2017-06-15T07:21:46Z", "raw_content": "", "timestamp_crawl": "2017-06-15T07:21:46Z", "_id": "http://effect.isi.edu/data/tweet/842127583022047232/extraction/HACKABLETHING/FINALLY", "doc_id": "http://effect.isi.edu/data/tweet/842127583022047232/extraction/HACKABLETHING/FINALLY"}])
            time.sleep(1)


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['my-topic'])

        for message in consumer:
            print (message)


def main():
    threads = [
        Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()

    time.sleep(10)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()