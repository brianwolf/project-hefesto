
def get_file_content(path: str) -> str:
    with open(path, 'rb') as file:
        return file.read()


def create_file(path: str, content: bytes):
    with open(path, 'w') as file:
        file.write(content)
