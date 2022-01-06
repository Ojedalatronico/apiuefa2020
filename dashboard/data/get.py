from config.api import url
import requests

print(url)
def get_all_team():
    return requests.get(url+"/all_teams").json()

def find_team(team):
    q = {
        "common_name":team
    }
    return requests.get(url+"/find/team", params=q).json()