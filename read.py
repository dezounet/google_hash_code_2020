IS_FIRST_LINE = True
IS_SECOND_LINE = False
SEPARATOR = ' '

from libraries import Library
from libraries import Book


def read(file_path):
    objects = []
    current_library = None

    with open(file_path, 'r') as file:
        first_line = True

        for index, line in enumerate(file):
            line = line.strip()

            line = list(line.split(SEPARATOR))
            if IS_FIRST_LINE:

                summary = line
                IS_FIRST_LINE = False
                IS_SECOND_LINE = True

            elif IS_SECOND_LINE:
                book_scores = line
                IS_SECOND_LINE = False

            else:
                if index % 2 == 0:
                    for book in line:
                        book_tmp = Book()
                        book_tmp.id = book
                        book_tmp.score = book_scores[book_tmp.id]
                        current_library.book_list.append(book_tmp)

                    objects.append(current_library)

                else:
                    library = Library()
                    library.books = line[0]
                    library.signing = line[1]
                    library.books_per_day = line[2]
                    current_library = library


    return summary, book_scores, objects

