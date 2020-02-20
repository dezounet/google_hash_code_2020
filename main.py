import os
import sys

from config import INPUT_DIRECTORY
from config import OUTPUT_DIRECTORY
from read import read
from score import get_best_score
from write import write


if __name__ == '__main__':

    # Get input file from command line arg list
    input_file = sys.argv[1]
    file_path = os.path.join(INPUT_DIRECTORY, input_file)
    assert os.path.exists(file_path)

    # Read data from input file
    data = read(file_path)

    initial_best_score = -1
    current_best_score = 0

    # TODO - get best score from output directory content
    best_scores = get_best_score()
    best_scores.get(input_file, 0)

    # TODO - algo !
    output = []


    # Save result to output file only if better solution found
    if initial_best_score < current_best_score:
        print('Better solution found for file %s! (+%s)' %
              (input_file,
              (current_best_score - initial_best_score)))

        output_file = os.path.splitext(input_file)[0] + '.out'
        out_path = os.path.join(OUTPUT_DIRECTORY, output_file)

        write(output, out_path)
    else:
        print('No better solution found :(')
