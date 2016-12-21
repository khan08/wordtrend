from __future__ import print_function, unicode_literals
import twitter

def getByTime():
    consumer_key = 'vNUbi4yAbUuZz1Huc2W6SSanW'
    consumer_secret = '4BqFg2irFjj8JsXAZjiI4cMfOfhvztD5Ol5AHI44Vcwz6VdYQa'
    access_token = '808772886035046401-Yry7I3IkNT1ujhtK2CJyeVYTZb5gxKK'
    access_token_secret = 'cexABmBwdjxkOrMQjf4fTRvAuNr5uGv0dfgd36tyNetgF'
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    return api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100&lang=en")




