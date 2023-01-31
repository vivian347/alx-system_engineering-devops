#!/usr/bin/python3
""" queries Reddit API """

import requests


def top_ten(subreddit):
    """ prints title of 1st 10 hot posts listed for a subreddit """
    headers = {
            'User-Agent': 'My Reddit API Client'
            }
    params = {
            "limit": 10
            }
    response = requests.get(
                            f'https://www.reddit.com/r/{subreddit}/hot.json',
                            headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_posts = [post['data']['title']
                     for post in data['data']['children']]
        for post in hot_posts:
            print(f"{post}")
    else:
        print("None")
