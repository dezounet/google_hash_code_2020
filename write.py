def write(libraries, file_path):
    with open(file_path, 'w') as f:
        f.write('%s\n' % (len(libraries)))

        for library in libraries:
            lib_id = library.id
            book_count = library.books_number
            f.write('%s %s\n' % (lib_id, book_count))
            f.write(' '.join(library.book_list))
            f.write('\n')
