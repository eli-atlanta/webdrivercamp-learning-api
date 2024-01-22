import requests

def delete_repo(url):
    header_authorization = {'Authorization': 'token <TOKEN>'}
    response = requests.delete(url, headers=header_authorization)
    print(f"Response status code: {response.status_code}")

if __name__=="__main__":
    owner = 'eli-atlanta'
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    delete_repo(url)