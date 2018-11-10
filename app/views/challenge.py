from flask import render_template, request

from app import app
from app.lib.utils import bin2str, str2bin


# Quest 1: Looking for the file
@app.route("/")
def challenge1():
    return render_template("welcome.html")


# Quest 2: Create a fuction
# Start edit code from this line

# Stop edit code below this line

# Quest 3: ...
# Start edit code from this line
@app.route("/b2s/<inp>")
def b2s():
    """Take binary numbers, convert to string

    Args:
        inp (str): binary number
    """
    return bin2str(inp)


@app.route("/s2b/<s>")
def s2b(s):
    """Take any string, convert to binary number

    Args:
        s (str): string
    """
    return str2bin()
# Stop edit code below this line


@app.route("/challenge3")
def challenge3():
    return render_template("challenge3.html")


@app.route("/hint1")
def hint1():
    data = {
        # Start edit code from this line
        "byte0": False,
        "byte1": False,
        "byte2": False,
        "byte3": False,
        "byte4": False,
        "byte5": False,
        "byte6": False,
        # Stop edit code below this line
    }
    return render_template("hint1.html", **data)


@app.route("/hint2")
def hint2():
    data = {
        "indexs": [58, 163, 61, 191, 3, 106],
        "letters": ['g', 'z', 'l', 'r', 'n', 'i', 'e', 'i', 'p', 's', 'a',
                    'r', 'x', 'r', 'j', 'z', 'b', 'h', 'p', 'a', 'c', 'v',
                    'q', 'm', 'i', 'u', 'v', 'h', 'u', 'm', 'b', 'd', 'c',
                    'p', 'e', 'd', 'm', 'n', 'z', 'e', 'g', 'w', 'b', 'd',
                    'z', 'f', 'a', 'x', 'r', 'z', 'm', 'p', 'o', 'k', 'q',
                    'o', 'k', 's', 'r', 'n', 'k', 't', 'g', 'w', 'g', 'y',
                    'b', 'e', 'r', 'd', 'm', 'u', 't', 'v', 'z', 'a', 'a',
                    'f', 's', 'y', 'n', 'm', 't', 'j', 'i', 'f', 'p', 'z',
                    'i', 'j', 'm', 'y', 'q', 'r', 'm', 'g', 'd', 'm', 'g',
                    'k', 'x', 'a', 'j', 'e', 'r', 'r', 'n', 'k', 'a', 'w',
                    'c', 'f', 'q', 'h', 'l', 'k', 'e', 'a', 't', 'j', 'b',
                    'k', 'k', 'm', 'j', 'c', 'p', 'j', 'y', 'b', 't', 'f',
                    'f', 'i', 'y', 'p', 'c', 'q', 'v', 'g', 'e', 'v', 'd',
                    'f', 'o', 'p', 'k', 'e', 'w', 'k', 'd', 'g', 't', 'x',
                    't', 'a', 't', 'm', 'q', 'u', 's', 'b', 'f', 'e', 'h',
                    'n', 'j', 's', 'x', 'z', 'c', 'h', 'u', 'x', 'c', 'k',
                    'u', 'i', 'y', 'k', 'x', 'c', 'w', 'm', 'd', 'q', 'i',
                    'w', 'j', 'c', 'z', 'u', 'h', 't', 's', 'r', 'm', 'k',
                    'b', 'z']
    }
    return render_template("hint2.html", **data)


def sum2(nums, target):
    """Part of Ultimate Quest"""
    dic = {}
    for idx, num in enumerate(nums):
        if num in dic:
            return [dic[num], idx]
        dic[target - num] = idx


    # Stop edit code below this line


@app.route("/ultimate_quest")
def ultimate_quest():
    test_cases = [
        {
            "target": 9,
            "list": [2, 7, 11, 13],
            "result": [0, 1]
        },
        {
            "target": 15,
            "list": [2, 7, 11, 13],
            "result": [0, 3]
        },
        {
            "target": 13,
            "list": [2, 7, 11, 13],
            "result": [0, 2]
        },
        {
            "target": 58,
            "list": [5, 23, 10, 53, 234, 1, 42, 18, 29, 3, 9, 25],
            "result": [0, 3]
        },
        {
            "target": 7,
            "list": [12, 2, 8, 3, 2, 9, 0, 7],
            "result": [6, 7]
        },
        {
            "target": 4,
            "list": [2, 3, 1],
            "result": [1, 2]
        },
        {
            "target": 4,
            "list": [2, 3, 7, 2],
            "result": [0, 3]
        },
    ]

    for case in test_cases:
        rst = sum2(case["list"], case["target"])
        case["real_result"] = rst

    data = {
        "test_cases": test_cases,
        "rst": all([case["result"] == case["real_result"]
                   for case in test_cases])
    }
    print(data)

    return render_template("ultimate_quest.html", **data)
