# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt","r") as readf:
        readf = readf.read()
    return readf
read_file_content("./story.txt")


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    use_text = text.split()
    
    count = {}
    for c in use_text:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count
count_words()

    #return {"as": 10, "would": 20}