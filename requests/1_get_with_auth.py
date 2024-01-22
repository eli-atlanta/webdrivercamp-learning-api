import requests

def get_with_auth(url):
    header_authorization = {'Authorization': 'token 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'}
    r = requests.get(url, headers=header_authorization)
    print(f"Response status code:", r.status_code)
    return len(r.json()), r.headers

if __name__=="__main__":
    url = "https://api.github.com/user/repos"

    num_of_repos, headers = get_with_auth(url)

    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")