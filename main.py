


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        wordcount(file_contents)
        lowerthecase(file_contents)
        
    return

def wordcount(file_contents):
    words = file_contents.split()
    count = len(words)
    print(f"This copy of Frankenstein contains {count} words.")
    return

def lowerthecase(words):
    lc_string = words.lower()
    # print(lc_string)
    return



    


main()