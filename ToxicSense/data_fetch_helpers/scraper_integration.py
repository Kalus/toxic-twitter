from twitterscraper.query import query_tweets, query_tweets_from_user

from data_fetch_helpers import tweet
from data_fetch_helpers.api_integration_base import ApiIntegration


class ScraperIntegration(ApiIntegration):

    def __init__(self):
        pass
    
    def get_user_tweets(self, username, limit):
        tweets = query_tweets_from_user(username, limit=limit)
        tweets.reverse()
        return tweet.Tweet.create_from_scraper_response(tweets)
    
    def get_tweets_from_search(self, search_term, limit):
        tweets = query_tweets(search_term, limit=limit)
        tweets.reverse()
        return tweet.Tweet.create_from_scraper_response(tweets)


api_integration = ScraperIntegration()
