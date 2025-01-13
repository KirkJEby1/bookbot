


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        wordcount(file_contents)
    return

def wordcount(file_contents):
    words = file_contents.split()
    count = len(words)
    print(f"This copy of Frankenstein contains {count} words.")
    

    


main()