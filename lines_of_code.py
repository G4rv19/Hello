import sys

def command_line():
    # user put no command line input (print too few command line arguments)
    if len(sys.argv) <= 1:
        print("Too few command-line arguments")
        return False

    # if user put too many command line input
    elif len(sys.argv) >= 3:
        print("Too many command-line arguments")
        return False

    # if user put a file without the py syntax
    elif not sys.argv[1].endswith(".py"):
        print("Not a python file.")
        return False

    # if user put a file name in cmd but it doesn't exist
    try:
        with open(sys.argv[1], "r"):
            pass
    except FileNotFoundError:
        print(f"The file '{sys.argv[1]}' does not exist.")
        return False

    return True

def main():
    if not command_line():
        return
    
    with open("bye.py", "r") as file:
        lines = file.readlines()
    
    count = 0
    for line in lines:
        if line.startswith("#"):
            continue
        line = line.strip()
        if line:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
