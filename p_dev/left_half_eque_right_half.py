# find the index at the sum of left = sum of right

input = [1,7,3,5,6]
## except return = 2

# if not then return -1 

def find_inex (input):
    # start with sum total
    current_total = sum(input)
    left_total  = 0
    for index, n in enumerate(input):
        right_total = current_total - left_total - n

        left_total += n

        if right_total == left_total:
            return index
    return -1
        
print(find_inex(input))