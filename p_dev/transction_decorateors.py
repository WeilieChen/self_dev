transactions = [

('Alex', 100),

('Chris', 200),

('Alex', -25),

('Sam', 300),

('Chris', 150),

('Alex', 75),

('Robin', 20)

    ]


def filter_transactions(transaction, threshold=50):
    filter_ls = []
    for trans in transaction:
        if abs(trans[1]) >= threshold:
            filter_ls.append(trans)
    return filter_ls
        

def combine_transactions(transaction):

    ls = filter_transactions(transaction)
    name_ls =[]
    ct = []
    for trans in ls:
        if trans[0] not in name_ls:
            name_ls.append(trans[0])
    for n in name_ls :
        amount = 0
        for trans in ls:
            if trans[0] == n:
                amount += trans[1]
        ct.append((n,amount))
    return ct
    

def sort_transactions(f):
    final_ls = combine_transactions(f)
    return sorted(final_ls,reverse=True)


print(sort_transactions(transactions))