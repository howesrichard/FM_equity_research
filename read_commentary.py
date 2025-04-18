def read_commentary(filepath):
    """
    Reads commentary from a .txt file and returns it as a string.
    """
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Commentary file not found."

# Test it
if __name__ == "__main__":
    path = "example_files/commentary.txt"
    content = read_commentary(path)
    print("COMMENTARY PREVIEW:\n")
    print(content)
