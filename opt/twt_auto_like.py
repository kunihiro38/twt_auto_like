""" ファイル実行で自動的にlikeを実行
「いいね」は24時間で1000件が上限で、それを超えるとペナルティ(アカウント停止等)を受ける
参考 http://docs.tweepy.org/en/latest/
"""

import os
import tweepy
import time

from dotenv import load_dotenv
load_dotenv()


CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def twt_auto_like():
    """ tweet_count 変数で設定した数だけ「いいね」を実行する
        search_list に「いいね」したい単語をリストに代入する
    """
    tweet_count = 50
    search_list = ['#python', '#ruby', '#php']

    for search in search_list:
        # サーチ結果
        search_result = api.search(q=search, count=tweet_count)
        for tweet in search_result:
            tweet_id = tweet.id
            try:
                # api.create_favorite(id=tweet_id)
                print('いいね!!をしました')
                time.sleep(3) 
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

if __name__ == "__main__":
    twt_auto_like()
