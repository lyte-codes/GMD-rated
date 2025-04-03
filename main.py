import requests

def find_rated_levels(diff):
    headers = {
        "User-Agent": ""
    }

    data = {
        "star": 1,
        "type": 0,
        "secret": "Wmfd2893gb7",
        "diff": diff
    }

    url = "http://www.boomlings.com/database/getGJLevels21.php"

    req = requests.post(url=url, data=data, headers=headers)
    output = req.text # Output of request

    for i in range(0,3):
        output = output[output.find("#") + 1:]

    output = output[0:output.find(":")]
    print(output)

find_rated_levels(1)
find_rated_levels(2)
find_rated_levels(3)
find_rated_levels(4)
find_rated_levels(5)
