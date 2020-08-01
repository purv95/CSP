import csv
import timeit


def read():
    with open('words4') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        temp = []
        for row in csv_reader:
            temp.append(row[0])
            line_count += 1
        return temp


def miss():
    with open('puzzle4') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        temp = []
        for row in csv_reader:
            temp.append(row[0])
            line_count += 1
        return temp


def findword(words, size):
    for i in range(len(words)):
        if len(words[i]) is size:
            word = words.pop(i)
            return str(word)


def findlen(word, loc):
    count = 0
    i = loc
    while (len(word)) != i and word[i] == '_':
        count += 1
        i += 1
    return count


def fill(words, missing):
    for i in range(len(missing)):
        loc = missing[i].find('_')
        while loc != -1:
            length = findlen(missing[i], loc)
            word = findword(words, length)
            missing[i] = missing[i][:loc] + word + missing[i][loc+len(word):]
            loc = missing[i].find('_')
    words.pop(-1)


def is_missing(missing):
    for word in missing:
        if word.find('_') is not -1:
            return True
    return False


def replace(word, missing):
    for i in range(len(missing)):
        loc = missing[i].find('_')

        if len(word) == findlen(missing[i], loc):
            missing[i] = missing[i][:loc] + word + missing[i][loc+len(word):]
            return True
    return False


def backtrack(words, missing):
    if not is_missing(missing):
        return True

    for w in words:
        words.remove(w)
        if replace(w, missing):
            if backtrack(words, missing):
                return True
        else:
            words.append(w)
    return False


def printstr(llist):
    for w in llist:
        print(w)


words = read()
missing = miss()

start = timeit.default_timer()
backtrack(words, missing)
stop = timeit.default_timer()

print("\n\n Puzzle filled\n")
printstr(missing)
print("\n")
print('Time: ', stop - start)

words = read()
missing = miss()

start = timeit.default_timer()
fill(words, missing)
stop = timeit.default_timer()

print("\n\n Puzzle filled\n")
printstr(missing)
print("\n")
print('Time: ', stop - start)
