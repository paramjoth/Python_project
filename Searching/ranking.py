accounts={'acc5': {'timestamp': 5, 'total_trans': 0, 'balance': 0}, 'acc4': {'timestamp': 29, 'total_trans': 4, 'balance': 215}, 'acc3': {'timestamp': 31, 'total_trans': 6, 'balance': 759}, 'acc2': {'timestamp': 30, 'total_trans': 6, 'balance': 58}}
#sorted(accounts, key=x[1]["total_trans"].get, reverse=True)
res = sorted(accounts.items(), key=lambda x: x[1]['total_trans'], reverse=True)

# print result
print(str(res))
