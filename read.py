SKIP_FIRST_LINE = False
SEPARATOR = ' '

def read(file_path):
    objects = []

    with open(file_path, 'r') as file:
        first_line = True
        for line in file:
            line = line.strip()

            if SKIP_FIRST_LINE and first_line:
                first_line = False
            else:
                elements = list(line.split(SEPARATOR))
                objects.append(elements)

    return objects
