import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            for child in children:
                title = child['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            print("Nothing")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Nothing")
