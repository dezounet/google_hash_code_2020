#!/usr/bin/env python
from score_library import score_libraries


def scan_books(libraries, method_name):

    # score and sort libraries
    lib_scores = score_libraries(libraries, method_name)
    lib_and_scores = zip(libraries, lib_scores)
    lib_and_scores = sorted(lib_and_scores, key=lambda ls: ls[1], reverse=True)

    sorted_libraries, _ = zip(*lib_and_scores)

    return sorted_libraries
