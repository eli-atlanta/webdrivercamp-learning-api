import requests

def get_created_repo(url):
    header_authorization = {'Authorization': 'token <TOKEN>'}
    r = requests.get(url, headers=header_authorization)
    print(f"Response status code:", r.status_code)
    repo = r.json()
    assert repo['has_wiki'] == False
    assert repo['private'] == True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'eli-atlanta'


if __name__=="__main__":
    owner = 'eli-atlanta'
    repo = 'repo-created-with-api'
    url = f"https://api.github.com/repos/{owner}/{repo}"

    get_created_repo(url)