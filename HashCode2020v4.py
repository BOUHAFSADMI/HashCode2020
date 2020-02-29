import math


class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Library:
    isSignedUp = False
    booksShipped = []
    books = []

    def __init__(self, id, num_books, signup_days, shipment_day, bookIds, score):
        self.id = id
        self.num_books = num_books
        self.signup_days = signup_days
        self.shipment_day = shipment_day
        self.bookIds = bookIds
        self.score = score


books = []
libraries = []
shippedBookIds = []
result = []  # containing library objects

[num_books, num_libs, days] = list(map(int, input().split()))

books_score = list(map(int, input().split()))

for i in range(0, num_libs):
    [num_books_lib, signup_days, shipment_day] = list(map(int, input().split()))
    bookIds = list(map(int, input().split()))
    score = sum([books_score[i] for i in bookIds])
    libraries.append(Library(i, num_books_lib, signup_days, shipment_day, bookIds, score))


libraries.sort(key=lambda x: x.score - (x.signup_days * x.shipment_day) * score/len(x.bookIds), reverse=True)

temp_days = 0

for lib in libraries:
    books = [bookId for bookId in lib.bookIds if bookId <= num_books]
    books_d = {x: books_score[x] for x in books}
    books_dict = {k: v for k, v in sorted(books_d.items(), key=lambda item: item[1], reverse=True)}
    if (len(books)) and days > 0:
        signup_days = lib.signup_days - temp_days
        if signup_days > 0:
            days -= signup_days
            temp_days = 0
        else:
            temp_days = temp_days - lib.signup_days
        days += temp_days
        num_days = lib.num_books / lib.shipment_day
        if math.ceil(num_days) > days:
            num_days = days
        temp_days += math.ceil(num_days)
        lib.booksShipped = [x for x in books_dict.keys() if x not in shippedBookIds]
        shippedBookIds.extend(lib.booksShipped)
        if len(lib.booksShipped):
            result.append(lib)

print(len(result))
for lib in result:
    print(lib.id, " ", len(lib.booksShipped))
    for id in lib.booksShipped:
        print(id, end=' ')
    print()
