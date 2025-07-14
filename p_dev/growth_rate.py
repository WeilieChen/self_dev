# n day
# total revenue target (xyz)
# day 1 value (D1v)

def focrecasting(n, xyn, d1v):
    growth_date = xyn / n

    for d in range(1, n+1):
        focrecast = d1v + d*growth_date
        print(focrecast)


focrecasting(10, 200000, 12321)