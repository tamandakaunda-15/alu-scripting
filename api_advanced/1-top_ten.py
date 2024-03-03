#!/usr/bin/python3
# prints titles of the first 10 hot posts
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            print(f"Top 10 hot posts in r/{subreddit}:\n")
            for post in children:
                print(post['data']['title'])
        else:
            print("None")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("None")
