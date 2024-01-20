def read_a_file(filename):
    f = open(filename, 'r')
    print(f.readlines()[2])


# YOUR CODE HERE

if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    read_a_file(file_name)