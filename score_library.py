#!/usr/bin/env python

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


