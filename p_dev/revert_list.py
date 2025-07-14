# l1 = ['2','4','3','null']
# l2 = ['5','6','4','null']

# output = ['7', '0' ,'8' , null]

# l1 = ['0', null]
# l2 = ['0', null]

# output  = ['0', null]

def revert_string(l):
    ### take the null out 
    non_null_l = [i for i in l if i != 'null']
    non_null_l.reverse()
    return non_null_l

def convert_ls_int(l):
    lt =revert_string (l)
    con_string = ''.join(lt)
    return int(con_string)

def adding_two(l1,l2):
    n1 = convert_ls_int(l1)
    print(n1)
    n2 = convert_ls_int(l2)
    print(n2)
    add_hum = str(n1+n2)
    split_lt = list(add_hum)
    split_lt.reverse()
    split_lt.append('null')
    

    return(split_lt)


###########
#############
###########

# Input: 
# l1 = [2,4,3] 
# l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: 
# l1 = [0]
# l2 = [0]
# Output: [0]
# Example 3:

# Input: 
# l1 = [0,0,0,9,9,9,9,9,9,9]
# l2 = [9,9,9,9,0]
# # Output: [8,9,9,9,0,0,0,1]


# class solution:

#     def remove_lead_0(self, lt:list):
#         for i in range(len(lt)):
#             if lt[i] != 0:
#                 return lt[i:]

#     def revert_ls(self,lt: list):
        
#         lt_ = self.remove_lead_0(lt)

#         lt_ret =[]


#         for i in lt_:
#             if 0 <= i <= 100:
#                 lt_ret.append(str(i))
        
#         lt_ret.reverse()
        
#         return lt_ret
        
#     def addTwoNumbers (self, l1:list,l2:list):
#         ### revert the list
#         l1new = self.revert_ls(l1)
#         l2new = self.revert_ls(l2)


#         num1 = ''.join(l1new)
#         num2 = ''.join(l2new)
#         final_num =  str(int(num1)+int(num2))
#         final_list  = list(final_num)
#         final_list.reverse()
#         return final_list

# so = solution()

# print(so.addTwoNumbers (l1,l2))


x = -123

def revers(num):
    x = abs(num)
    revers_x = str(x)[::-1]
    lt_revers = list(revers_x)

    ## check 0
    lt_new = []
    for i in lt_revers:
        if i != '0':
            lt_new.append(i)
    
    if num > 0 :
        return int(''.join(lt_new))
    else :
        return - int(''.join(lt_new))


print(revers(x))

