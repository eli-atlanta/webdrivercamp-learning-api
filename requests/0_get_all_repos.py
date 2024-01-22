import requests

def get_repos(url):
    response = requests.get(url)
    print(f"Response status Code:", response.status_code)
    print(f"Total count of found items:", response.json()['total_count'])
    before_list = response.json()['items']
    return sorted(before_list, key=lambda x: x['full_name'])



if __name__=="__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"

    list_of_items = get_repos(url)
    print()

    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']

        print(f"{user:15}", repo)