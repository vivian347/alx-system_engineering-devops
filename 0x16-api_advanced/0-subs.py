#!/usr/bin/python3

"""queries the Reddit API """


import requests


def number_of_subscribers(subreddit):
    """ returns number of subs"""
    headers = {
            'User-Agent': 'My Reddit API Client'
            }
    response = requests.get(
                            f'https://www.reddit.com/r/{subreddit}/about.json',
                            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
