import datetime as dt
import logging
import random
import re
import time
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

from data_fetch_helpers import constants as data_fetch_constants
from data_fetch_helpers import public as data_fetch_public

logger = logging.getLogger('toxicsense.clientapp.views')

def home(request):
    return render(
        request,
        'clientapp/home.html',
        {
            'title': 'ToxicSense',
        }
    )


def analyze_topic(request):
    search_term = request.GET.get('topic')
    tweets, error = data_fetch_public.get_tweets_from_search(
        search_term, 300, data_fetch_constants.DATA_SOURCE_TWEEPY
    )
    if error:
        return JsonResponse({
            'error': error
        }, safe=False)
    logger.info('Analyzing toxicity of results')
    start = time.time()
    result = [tweet.to_dict() for tweet in tweets]
    end = time.time()
    logger.info('Took ' + str(end - start) + ' seconds')
    return JsonResponse(result, safe=False)


def analyze_user(request):
    user = request.GET.get('user')
    user_clean = re.sub("[^A-Za-z_]", "", user)
    user_clean = user_clean if len(user_clean) < 15 else user_clean[0:15]
    tweets, error = data_fetch_public.get_tweets_of_user(
        user_clean, 100, data_fetch_constants.DATA_SOURCE_TWEEPY
    )
    if error:
        return JsonResponse({
            'error': error
        }, safe=False)
    logger.info('Analyzing toxicity of results')
    start = time.time()
    result = [
        tweet.to_dict()
        for tweet in tweets
        if tweet.user == user
    ]
    end = time.time()
    logger.info('Took ' + str(end - start) + ' seconds')
    return JsonResponse(result, safe=False)


def analyze_tweet(request):
    url = request.GET.get('tweet_url')
    try:
        # We except it to be of form https://twitter.com/username/status/1064734907940994497
        url_fragments = url.rstrip('/').rsplit('/', 3)
        tweet_id = url_fragments[-1]
        user = url_fragments[-3]
    except:
        return JsonResponse({
            'error': True
        }, safe=False)
    replies, error = data_fetch_public.get_replies_of_tweet(
        tweet_id, user, 100, data_fetch_constants.DATA_SOURCE_TWITTER_API
    )
    if error:
        return JsonResponse({
            'error': error
        }, safe=False)
    logger.info('Analyzing toxicity of results')
    start = time.time()
    result = [
        reply.to_dict()
        for reply in replies
    ]
    end = time.time()
    logger.info('Took ' + str(end - start) + ' seconds')
    return JsonResponse(result, safe=False)
