
def get_file_content(path: str) -> str:
    with open(path, 'rb') as file:
        return file.read()
