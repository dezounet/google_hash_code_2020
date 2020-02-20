#!/usr/bin/env python


def simple_library_score(library):

    b_scores = []
    for b in library.book_list:
        b_scores.append(b.score)
    lib_score = sum(b_scores) / float(len(b_scores)) * library.books_per_day
    return lib_score
