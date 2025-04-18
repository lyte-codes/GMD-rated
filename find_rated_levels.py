import requests

def find_rated_levels(diff):
    # request info
    url = "http://www.boomlings.com/database/getGJLevels21.php"

    headers = {
        "User-Agent": ""
    }

    data = {
        "star": 1,
        "type": 0,
        "secret": "Wmfd2893gb7",
        "diff": diff
    }

    if (diff == -1):
        data = {
            "star": 1,
            "type": 0,
            "secret": "Wmfd2893gb7",
        }
    
    # request parsing
    req = requests.post(url=url, data=data, headers=headers)
    output = req.text # Output of request

    for i in range(0,3):
        output = output[output.find("#") + 1:]

    output = output[0:output.find(":")]
    return output

import requests

def account_beat_rated_levels():
    url = "http://www.boomlings.com/database/getGJUserInfo20.php"
    
    data = {
        "secret": "Wmfd2893gb7",
        "targetAccountID": "29968314"
    }
    headers = {
        "User-Agent": ""
    }

    req = requests.post(url, data=data, headers=headers)
    output = req.text

    # Split and pair up the output
    parts = output.split(':')
    paired = [parts[i] + ':' + parts[i + 1] for i in range(0, len(parts) - 1, 2)]

    # If there's an odd leftover part, add it
    if len(parts) % 2 == 1:
        paired.append(parts[-1])

    # Remove last item if it's not key 55, 56, or 57
    if ':' in paired[-1] and paired[-1].split(':')[0] not in ['55', '56', '57']:
        paired.pop()

    # Initialize
    acc55 = acc56 = acc57 = None
    rated = [0] * 6

    # Process key:value pairs
    for pair in paired:
        if ':' not in pair:
            continue

        key, value = pair.split(':', 1)

        if key == '55':
            acc55 = value.split(',')
        elif key == '56':
            acc56 = value.split(',')
        elif key == '57':
            acc57 = value.split(',')

    # Fill the rated list with sum of acc56 and acc57 values
    for i in range(0, 5):
        rated[i] = int(acc56[i]) + int(acc57[i])

    return rated