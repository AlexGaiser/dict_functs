from itertools import permutations

w = open('words.txt')

dictionary = list(w.read().rstrip().splitlines())

# print(dictionary)

def anagram_maker(word):
    w = open('words.txt')

    dictionary = list(w.read().rstrip().splitlines())
    # print(dictionary)
    perms = list([''.join(p) for p in permutations(word.lower())])
    # print(perms)
    # print(perms)
    for permutation in perms:
        # print(permutation)
        if permutation in dictionary:
            print('anagram : ' + permutation) 


def isogram_finder(wordlist):
    wordlist = list(map(str.lower, wordlist))
    isogram = True
    isogramlist = []
    for word in wordlist:
        isogram = True
        for char in word: 
            if word.count(char) > 1:
                isogram = False
                break
        if isogram == True:
            isogramlist.append(word)
    return isogramlist


all_iso = isogram_finder(dictionary)

