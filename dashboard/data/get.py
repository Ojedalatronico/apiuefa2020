from config.api import url
import requests

print(url)
def get_all_team():
    return requests.get(url+"/all_teams").json()