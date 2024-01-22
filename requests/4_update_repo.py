import requests

def update_repo(url):
    header_authorization = {'Authorization': 'token <TOKEN>'}
    myobj = {'description': 'I know Python Requests'}
    r = requests.patch(url, headers=header_authorization, json=myobj)
    print(f"Response Status code: {r.status_code}")

    repo = r.json()
    return repo



if __name__=='__main__':
    url = 'https://api.github.com/repos/eli-atlanta/repo-created-with-api'

    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests'