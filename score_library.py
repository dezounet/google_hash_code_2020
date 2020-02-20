#!/usr/bin/env python

import numpy as np


def _simple_library_score(library):
    b_scores = []
    for b in library.book_list:
        b_scores.append(b.score)
    lib_score = sum(b_scores) / float(len(b_scores)) * library.books_per_day
    return lib_score


def simple_libraries_score(libraries):
    l_scores = []
    for l in libraries:
        l_scores.append(simple_libraries_score())
    return l_scores


SCORE_FN = {
    'simple_score': simple_libraries_score
}


def score_libraries(libraries, method_name):
    return SCORE_FN[method_name](libraries)


def library_score(library, book_occurences, scanned_books):
    b_scores = []
    library_book_occurences = []
    for index, b in enumerate(library.book_list):
        b_scores.append(b.score)
        library_book_occurences[index] = book_occurences[b.id]

    numerator = sum([b_scores[i]/float(library_book_occurences[i]) for i in range(len(b_scores)) if library.book_list[i].id not in scanned_books])*library.books_per_day
    lib_score = numerator/float(len(b_scores))
    return lib_score

