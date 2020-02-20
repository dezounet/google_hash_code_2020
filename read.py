from libraries import Library
from libraries import Book


def read(file_path):
    IS_FIRST_LINE = True
    IS_SECOND_LINE = False
    SEPARATOR = ' '

    objects = []
    current_library = None
    book_occurrences = list()

    with open(file_path, 'r') as file:

        for index, line in enumerate(file):
            line = line.strip()

            line = list(line.split(SEPARATOR))
            if IS_FIRST_LINE:
                summary = line
                IS_FIRST_LINE = False
                IS_SECOND_LINE = True

            elif IS_SECOND_LINE:
                book_scores = line
                book_occurrences = [0] * len(book_scores)

                IS_SECOND_LINE = False

            else:
                if index % 2 == 1:
                    for book in line:
                        book = int(book)
                        
                        book_tmp = Book(book, book_scores[book])
                        current_library.book_list.append(book_tmp)

                        # Update book_occcurrences table
                        book_occurrences[book] += 1

                    objects.append(current_library)

                else:
                    _id = int(index/2) - 1
                    _books = line[0]
                    _signing = line[1]
                    _books_per_day = line[2]
                    library = Library(_id, _books, _signing, _books_per_day)
                    current_library = library

    return summary, book_scores, book_occurrences, objects

