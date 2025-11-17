import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url, timeout=10)

# Check request success
response.raise_for_status()

pulls = response.json()

for pr in pulls:
    print(pr["user"]["login"])
