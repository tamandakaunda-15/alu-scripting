import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "MyRedditScrapperBot/1.0"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            print("Subreddit not found.")
            return 0
        elif response.status_code != 200:
            print(f"Unexpected status code: {response.status_code}")
            return 0

        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage:
subreddit_name = "python"
print("Subreddit:", subreddit_name)
print("Subscribers:", number_of_subscribers(subreddit_name))
