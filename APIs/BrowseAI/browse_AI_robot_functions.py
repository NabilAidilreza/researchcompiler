import requests
import json

def get_robot(robot_id,SECRET_API_KEY):
    # Returns the robot info #
    url = "https://api.browse.ai/v2/robots/{}".format(robot_id)

    Token = 'Bearer ' + SECRET_API_KEY

    headers = {"Authorization": Token}

    response = requests.request("GET", url, headers=headers)

    json_string = response.text

    data = json.loads(json_string)

    return data

def print_json(data):
    print(json.dumps(data, indent=4)) # JSON Prettify

# Example payload #
# payload = {"inputParameters": {"originUrl" : "Soccer", "Organic Result_limit": 5}}
# Input_paramters -> dictionary
def create_robot_task(robot_id, input_parameters, SECRET_API_KEY):
    # Sends a POST request to BROWSE AI to run the bot with the given input #
    url = "https://api.browse.ai/v2/robots/{}/tasks".format(robot_id)

    Token = 'Bearer ' + SECRET_API_KEY

    headers = {"Authorization": Token}

    payload = input_parameters

    response = requests.request("POST", url, json=payload, headers=headers)

    json_string = response.text

    data = json.loads(json_string)

    return data

def get_robot_tasks(robot_id, SECRET_API_KEY):
    url = "https://api.browse.ai/v2/robots/{}/tasks".format(robot_id)

    querystring = {"page":"1"}

    Token = 'Bearer ' + SECRET_API_KEY

    headers = {"Authorization": Token}

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_string = response.text

    data = json.loads(json_string)

    return data

def get_robot_task(robot_id, task_id, SECRET_API_KEY):
    # Returns the status of the robot task #
    url = "https://api.browse.ai/v2/robots/{}/tasks/{}".format(robot_id,task_id)

    Token = 'Bearer ' + SECRET_API_KEY

    headers = {"Authorization": Token}

    response = requests.request("GET", url, headers=headers)

    json_string = response.text

    data = json.loads(json_string)

    return data

def get_latest_robot_task(robot_id, SECRET_API_KEY):
    # Return an array of tasks
    data = get_robot_tasks(robot_id, SECRET_API_KEY)

    latest_task_JSON = data["result"]["robotTasks"]["items"][-1]
    latest_task_id = latest_task_JSON["id"]
    latest_task_results = latest_task_JSON["capturedLists"]

    return latest_task_id, latest_task_results

def process_robot_task_data(data_input):
    temp = []
    data = data_input[1] # get_latest_robot_task(robot_id,SECRET_API_KEY)[1]
    top_keys = data.keys()
    for key in top_keys:
        if data[key] != []: # if Main list is found #
            for element in data[key]:
                new_item = []
                for main_keys in element.keys():
                    new_item.append(element[main_keys])
                temp.append(new_item)
    return temp


