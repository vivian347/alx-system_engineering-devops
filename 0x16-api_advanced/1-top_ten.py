#!/usr/bin/python3
""" queries Reddit API """

import requests


def top_ten(subreddit):
    """ prints title of 1st 10 hot posts listed for a subreddit """
    headers = {
            'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
            }
    params = {
            "limit": 10
            }
    response = requests.get(
                            f'https://www.reddit.com/r/{subreddit}/hot.json',
                            headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
