# 2
# Python Programming,Programming,4.5
# Data Science Essentials,Data Science,4.2
# 2
# Programming

# Highest Rated Book: Python Programming, Rating: 4.5
# Highest Rated Book: Data Science Essentials, Rating: 4.2
# Top Recommended Book in Programming Genre: Python Programming, Rating: 4.5

# 3
books = ['Python Programming,Programming,4.5',
'Data Science Essentials,Data Science,4.2',
'C++ Programming,Programming,4.3']
n = 10
genre =  'Programming'

# Highest Rated Book: Python Programming, Rating: 4.5
# Highest Rated Book: C++ Programming, Rating: 4.3
# Top Recommended Book in Programming Genre: Python Programming, Rating: 4.5

import random

def book_add(books:list):
    inv = []
    for book in books:
        booklt = book.split(',')
        book_ob ={
            'title' : booklt[0],
            'genre' : booklt[1],
            'rating' : float(booklt[2])
        }
        inv.append(book_ob)
    return inv

def book_reco(books,n,genre):

    inv = book_add(books)

    ### filter the list base of genre
    rec_ls =[]
    left_inv =[]
    for book in inv :
        if book['genre'] == genre:
            rec_ls.append(book)
        else:
            left_inv.append(book)

    rankbook = sorted(rec_ls, key=lambda x:x['rating'],reverse=True)


    if len(rankbook) < n:
        mis = n - len(rankbook)
        rankbook.append(left_inv[:mis])
        rec_final=rankbook

    else:
        rec_final = rankbook[:n]

    return rec_final
    

print(book_reco(books,n,genre))