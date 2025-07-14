""" From a given list of book titles, 
identify sequels (e.g., for an input like ['GOT', 'Troy', 'Batman', 'Batman Returns'], 
the output should be ['Batman Returns']). """

def solution(ls):
    i=0
    for i in range(len(ls)-1):
       if ls[i+1].startswith(ls[i]):
           return  ls[i+1]
       else:
           i+=1

solution(['GOT', 'Troy', 'Batman', 'Batman Returns'])

