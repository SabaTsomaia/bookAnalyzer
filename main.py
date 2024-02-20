path_to_file = "books/frankenstein.txt"


def __main__():
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

