#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
    Hint:   No authentication is necessary for most features of the Reddit API.
            If you’re getting errors related to Too Many Requests,
            ensure you’re setting a custom User-Agent.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    data = response.json().get('data')
    return data.get('subscribers')
