import math
import os
from statistics import mean
from statistics import stdev

from config import INPUT_DIRECTORY
from libraries import Library
from libraries import Book
from read import read


def print_statistics(elements, label):
    elements = list(map(int, elements))
    mean_elements = mean(elements)
    stdev_elements = stdev(elements)
    min_elements = min(elements)
    max_elements = max(elements)

    print('mean', label, ':', mean_elements)
    print('std dev', label, ':', stdev_elements)
    print('min', label, ':', min_elements)
    print('max', label, ':', max_elements)


if __name__ == '__main__':

    for filename in os.listdir(INPUT_DIRECTORY):
        if not filename.startswith('.'):
            filename = os.path.join(INPUT_DIRECTORY, filename)
            inputs = read(filename)

            # Overall analytics
            lib_count = inputs[0][1]
            book_count = inputs[0][0]
            days = inputs[0][2]

            print(
                'file %s: %s lib, %s books, %s days' %
                (os.path.basename(filename),
                 lib_count,
                 book_count,
                 days)
            )

            # Book analytics
            print('sum of book score:', sum(map(int, inputs[1])))
            print_statistics(inputs[1], 'book')

            # Lib analytics
            inputs = inputs[2:]

            book_count = []
            signup_durations = []
            capacity = []

            for i in range(math.floor(len(inputs) / 2)):
                lib_id = i * 2
                book_id = i * 2 + 1

                lib_info = inputs[lib_id]
                book_info = inputs[book_id]
                book_count.append(lib_info[0])
                signup_durations.append(lib_info[1])
                capacity.append(lib_info[2])

            print_statistics(book_count, 'lib book count')
            print_statistics(signup_durations, 'lib signup diration')
            print_statistics(capacity, 'lib capacity')

            print('======================================================')
            print()
