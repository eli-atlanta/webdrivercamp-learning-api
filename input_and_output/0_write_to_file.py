def write_to_file(data, filename):
    length = 0
    with open(filename, 'w') as file_write:
        file_write.write(data)

    with open(filename, 'r') as file_read:
        for line in file_read:
            length += len(line)

    return length

# YOUR CODE HERE

if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    data = """
    In the beginning the Universe was created. 
    This has made a lot of people very angry and been widely regarded as a bad move."""

    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    print()
    print(f"Number of char: {write_to_file(data, file_name)}")
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    print()
    data = "Don't Panic"
    print(f"Number of char: {write_to_file(data, file_name)}")
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")