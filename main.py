


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        wordcount(file_contents)
        nocaps = lowerthecase(file_contents)
        dict_count = charcount(nocaps)
        #print(nocaps)
        print(dict_count)
        
    return

def wordcount(file_contents):
    words = file_contents.split()
    count = len(words)
    print(f"This copy of Frankenstein contains {count} words.")
    return 

def lowerthecase(words):
    lc_string = words.lower()
    # print(lc_string)
    return lc_string

def charcount(nocaps):
    chardict = {}
    for i in nocaps:
        chardict[i] = chardict.get(i,0)+1
    return chardict



    


main()