def solution(queries):
    output = []
    accounts = {}
    for query in queries:
        operation = query[0]
        if operation == "CREATE_ACCOUNT":
            account_id = query[2]
            timestamp = int(query[1])
            if account_id not in accounts:
                accounts[account_id] = {"balance": 0, "timestamp": timestamp, "total_trans_amount": 0}
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
                accounts[account_id]["total_trans_amount"] += amount
                output.append(str(accounts[account_id]["balance"]))
            else:
                output.append("")
        elif operation == "PAY":
            account_id = query[2]
            amount = int(query[3])
            timestamp = int(query[1])
            if account_id in accounts:
                if accounts[account_id]["balance"] >= amount:
                    accounts[account_id]["balance"] -= amount
                    accounts[account_id]["timestamp"] = timestamp
                    accounts[account_id]["total_trans_amount"] += amount
                    output.append(str(accounts[account_id]["balance"]))
                else:
                    output.append("")
            else:
                output.append("")
        elif operation == "TOP_ACTIVITY":
            timestamp = int(query[1])
            n = int(query[2])
            top_accounts = sorted(accounts.items(), key=lambda x: (-x[1]["total_trans_amount"], x[0]))[:n]
            top_accounts_str = ", ".join(["{}({})".format(a[0], a[1]["total_trans_amount"]) for a in top_accounts])
            output.append(top_accounts_str)

    return output

