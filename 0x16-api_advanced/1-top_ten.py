#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Custom'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        for post in children[:10]:
            print(post.get('data').get('title'))
    else:
        print(None)
