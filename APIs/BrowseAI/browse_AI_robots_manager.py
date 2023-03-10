import requests
import json

SECRET_API_KEY = 'INSERT YOUR SECRET API KEY FROM BROWSE.AI'

Google_Search_Robot_ID = 'INSERT ROBOT ID FROM BROWSE AI' # Input required is search_term and max_results_no -> {"inputParameters": {"originUrl" : "Soccer", "Organic Result_limit": 5}}
Reddit_Search_Robot_ID = 'INSERT ROBOT ID FROM BROWSE AI' # Input required is reddit_subreddit and max_results_no -> {"inputParameters": {"originUrl" : "https://www.reddit.com/user/OfficialSGExams/", "Posts_limit": 5}}
Country_Trends_Robot_ID = 'INSERT ROBOT ID FROM BROWSE AI' # Input required is uppercase country abbreviation like US, CA and UK -> {"inputParameters": {"originUrl" : "SG"}}
Google_Scholars_Robot_ID = 'INSERT ROBOT ID FROM BROWSE AI' # Input required is search_term and max_results_no -> {"inputParameters": {"search_keyword" : "Blockchain", "articles_list_limit": 5}}

def get_all_robots(SECRET_API_KEY):
    Token = 'Bearer ' + SECRET_API_KEY

    headers = {"Authorization": Token}

    url = "https://api.browse.ai/v2/robots"

    response = requests.request("GET", url, headers=headers)

    json_string = response.text

    data = json.loads(json_string)

    print(json.dumps(data, indent=4)) # JSON Prettify

def get_secret_api_key():
    return SECRET_API_KEY

def get_robot_app(term):
    if term == "Google Search":
        return Google_Search_Robot_ID
    elif term == "Reddit Search":
        return Reddit_Search_Robot_ID
    elif term == "Country Trends":
        return Country_Trends_Robot_ID
    elif term == "Google Scholar":
        return Google_Scholars_Robot_ID

#get_all_robots(SECRET_API_KEY)