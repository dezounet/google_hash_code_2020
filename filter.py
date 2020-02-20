def filter_books(libraries):
    books = set()
    for lib in libraries:
        current_books = set(lib.book_list)
        relevant_books = current_books - books
        books.union(relevant_books)
        relevant_books = list(relevant_books)
        
        lib.book_list = relevant_books
        lib.books_number = len(relevant_books)
