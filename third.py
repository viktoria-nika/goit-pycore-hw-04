import sys
from colorama import Back

def read_file_contents(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    print(Back.GREEN + read_file_contents("second_2.txt"))
else:
    print("Error: provide file path")