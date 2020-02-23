#!/usr/bin/env python

import numpy as np
import copy

from filter import filter_books


def _simple_library_score(library):
    b_scores = []
    for b in library.book_list:
        b_scores.append(int(b.score))
    lib_score = sum(b_scores) / float(len(b_scores)) * int(library.books_per_day)
    return lib_score


def simple_libraries_score(libraries):
    l_scores = []
    for l in libraries:
        l_scores.append(_simple_library_score(l))
    return l_scores


def improved_libraries_score(libraries):
    l_scores = []
    for l in libraries:
        l_scores.append(_simple_library_score(l) / float(l.signing))
    return l_scores


def score_libraries_by_capacity(libraries):
    l_scores = []
    for l in libraries:
        l_scores.append(l.books_per_day)
    return l_scores


def library_score(library, book_occurences, scanned_books):
    b_scores = []
    library_book_occurences = []
    for index, b in enumerate(library.book_list):
        b_scores.append(b.score)
        library_book_occurences[index] = book_occurences[b.id]

    numerator = sum([b_scores[i]/float(library_book_occurences[i]) for i in range(len(b_scores)) if library.book_list[i].id not in scanned_books])*library.books_per_day
    lib_score = numerator/float(len(b_scores))
    return lib_score


def iterative_select_libraries(libraries, total_days):

    remaining_libs = copy.deepcopy(libraries)
    elasped_days = 0
    while elasped_days < int(total_days):
        remain_scores = improved_libraries_score(remaining_libs)
        remaining_libs = sort_lib_scores(remaining_libs, remain_scores)
        lib_choice = remaining_libs.pop(0)
        elasped_days += int(lib_choice.signing)
        filter_books(remaining_libs)

    return remaining_libs


def sort_lib_scores(libraries, scores):
    lib_and_scores = zip(libraries, scores)
    lib_and_scores = sorted(lib_and_scores, key=lambda ls: ls[1], reverse=True)
    sorted_libraries, _ = zip(*lib_and_scores)
    return list(sorted_libraries)


SCORE_FN = {
    'simple_score': simple_libraries_score,
    'capacity_score': score_libraries_by_capacity,
    'improved_simple_score': improved_libraries_score,
    'iterative_select': iterative_select_libraries
}


def score_libraries(libraries, method_name, total_days):
    return SCORE_FN[method_name](libraries, total_days)


#
# def greedy_choose_libraries(libraries):
#     selected_libraries = []
#
#     for i in range(len(libraries)):
#

