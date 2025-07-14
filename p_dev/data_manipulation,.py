ls = [
    {'id' : 1, 
    'value': '10'},
    {'id' : 2, 
    'value': 'abc'},
]

def value_check(ls:list):
    
    final_ls =[]
    for i in ls:
        dict = {}
        dict['id'] = i['id']
        check_v =  i['value'] 
        if isinstance(check_v,int):
            dict['value']=int(check_v)
        else:
            dict['value']=0
            
        final_ls.append(dict)
    return final_ls


print(value_check(ls))


### count error 
ls_error = ['2025-04-01 ERROR', '2025-04-02 info','2025-04-02 ERROR']

def count_error (ls_error: list):
    ct = 0
    for i in ls_error:
        if i.endswith('ERROR'):
            ct += 1
    return ct

print(count_error(ls_error))