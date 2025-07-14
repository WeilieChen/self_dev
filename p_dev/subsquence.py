# input s = "xyz"
# return ['x', 'xy', 'xyz', 'xz', 'y', 'yz', 'z']


def buildSubsequences(s):
    
    output =[]
    output.append(s)
    ## split string to list
    lt = list(s)

    ## ['x','y','z']    
    ## start iteration with x , on ['y','z']
    for index, i in enumerate(lt):
        output.append(i)
        for e in lt[index:]:
            if i != e:
                output.append(i+e)
    return (sorted(output))
        