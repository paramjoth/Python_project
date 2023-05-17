def solution(queries):
    accounts = {}
    output = []
    for query in queries:
        operation = query[0]
        #timestamp = int(query[1])
        if operation == "CREATE_ACCOUNT":
            account_id = query[2]
            timestamp = int(query[1])
            if account_id not in accounts:
                accounts[account_id] = {"balance": 0, "timestamp": timestamp}
                output.append("true")
            else:
                output.append("false")
        elif operation == "DEPOSIT":
            account_id = query[2]
            amount = int(query[3])
            timestamp = int(query[1])
            if account_id in accounts:
                accounts[account_id]["balance"] += amount
                accounts[account_id]["timestamp"] = timestamp
                output.append(str(accounts[account_id]["balance"]))
            else:
                #account_id = query[2]
                #accounts[account_id] = {"balance": 0, "timestamp": timestamp}
                #accounts[account_id]["balance"] += amount
                #accounts[account_id]["timestamp"] = timestamp
                #output.append(accounts[account_id]["balance"])
                output.append("")
        elif operation == "PAY":
            account_id = query[2]
            amount = int(query[3])
            timestamp = int(query[1])
            if account_id in accounts:
                if accounts[account_id]["balance"] >= amount:
                    accounts[account_id]["balance"] -= amount
                    accounts[account_id]["timestamp"] = timestamp
                    output.append(str(accounts[account_id]["balance"]))
                else:
                    output.append("")
            else:
                output.append("")
    return output


queries = [
  ["CREATE_ACCOUNT", "1", "account1"],
  ["CREATE_ACCOUNT", "2", "account1"],
  ["CREATE_ACCOUNT", "3", "account2"],
  ["DEPOSIT", "4", "non-existing", "2700"],
  ["DEPOSIT", "5", "account1", "2700"],
  ["PAY", "6", "non-existing", "2700"],
  ["PAY", "7", "account1", "2701"],
  ["PAY", "8", "account1", "200"]
]

print(solution(queries))

queries2= [
    [
        "CREATE_ACCOUNT",
        "2",
        "acc2"
    ],
    [
        "CREATE_ACCOUNT",
        "3",
        "acc3"
    ],
    [
        "CREATE_ACCOUNT",
        "4",
        "acc4"
    ],
    [
        "CREATE_ACCOUNT",
        "5",
        "acc5"
    ],
    [
        "DEPOSIT",
        "6",
        "acc1",
        "125"
    ],
    [
        "DEPOSIT",
        "7",
        "acc4",
        "633"
    ],
    [
        "DEPOSIT",
        "8",
        "acc1",
        "70"
    ],
    [
        "DEPOSIT",
        "9",
        "acc1",
        "475"
    ],
    [
        "DEPOSIT",
        "10",
        "acc2",
        "190"
    ],
    [
        "DEPOSIT",
        "11",
        "acc2",
        "15"
    ],
    [
        "DEPOSIT",
        "12",
        "acc4",
        "222"
    ],
    [
        "DEPOSIT",
        "13",
        "acc3",
        "859"
    ],
    [
        "DEPOSIT",
        "14",
        "acc2",
        "75"
    ],
    [
        "DEPOSIT",
        "15",
        "acc3",
        "100"
    ],
    [
        "DEPOSIT",
        "16",
        "acc2",
        "339"
    ],
    [
        "PAY",
        "17",
        "acc1",
        "5"
    ],
    [
        "PAY",
        "18",
        "acc2",
        "67"
    ],
    [
        "PAY",
        "19",
        "acc3",
        "11"
    ],
    [
        "PAY",
        "20",
        "acc3",
        "239"
    ],
    [
        "PAY",
        "21",
        "acc1",
        "125"
    ],
    [
        "PAY",
        "22",
        "acc3",
        "61"
    ],
    [
        "PAY",
        "23",
        "acc4",
        "45"
    ],
    [
        "PAY",
        "26",
        "acc1",
        "125"
    ],
    [
        "PAY",
        "27",
        "acc1",
        "45"
    ],
    [
        "PAY",
        "28",
        "acc1",
        "128"
    ],
    [
        "PAY",
        "29",
        "acc4",
        "595"
    ],
    [
        "PAY",
        "30",
        "acc2",
        "494"
    ],
    [
        "DEPOSIT",
        "31",
        "acc3",
        "111"
    ]
]

print(solution(queries2))
