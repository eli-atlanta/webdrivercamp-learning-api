import requests
from pprint import pprint

def create_repo(url):
    header_authorization = {'Authorization': 'token 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'}
    myobj = {'name': 'repo-created-with-api', 'private': True, 'has_wiki': False}
    r = requests.post(url, headers=header_authorization, json=myobj)

    print(f"Response status code: {r.status_code}")
    return r.json()


if __name__=='__main__':
    url = 'https://api.github.com/user/repos'

    repo = create_repo(url)
    pprint(repo)