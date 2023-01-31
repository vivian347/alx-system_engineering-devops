#!/usr/bin/python3

"""queries the Reddit API """


import requests


def number_of_subscribers(subreddit):
    """ returns number of subs"""
    headers = {
            'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
            }
    response = requests.get(
                            f'https://www.reddit.com/r/{subreddit}/about.json',
                            headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
