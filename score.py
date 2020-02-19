import os

from config import INPUT_DIRECTORY
from config import OUTPUT_DIRECTORY


def get_best_score():
    best_scores = {}

    for output_filename in os.listdir(OUTPUT_DIRECTORY):
        if output_filename.startswith('.'):
            continue

        current_score = 0

        input_filename = get_input_from_output(output_filename)

        best_scores[input_filename] = current_score

    return best_scores


def get_input_from_output(output_filename):
    # Compute input filename from output filename
    input_filename = os.path.splitext(output_filename)[0]

    return input_filename


if __name__ == '__main__':
    best_scores = get_best_score()

    total_score = 0
    for filename, score in best_scores.items():
        print('%s score: %s' % (filename, score))
        total_score += score

    print('===> total score: %s' % total_score)
