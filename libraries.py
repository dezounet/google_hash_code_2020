#!/usr/bin/env python


class Library:

    def __init__(self, id, book_number, signing, books_per_day):
        """

        :param books: list of Books
        :param signing: signing delay (int)
        :param books_per_day: int
        """
        self.id = id
        self.books_number = book_number
        self.signing = signing
        self.books_per_day = books_per_day
        self.book_list = dict()
        self.score = 0


    def library_set_score(self):

        processed_score = 0

        self.score = processed_score




class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
