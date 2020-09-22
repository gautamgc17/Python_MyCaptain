#Python code to create a function that takes a string
#And prints the letters in decreasing order of frequency

def most_frequent():

    str = input('Enter a string: ')
    dict = {}

    for line in str:
        words = line.split()
        for word in words:
            dict[word] = dict.get(word,0) + 1

    y = sorted([(v,k) for k,v in dict.items()],reverse = True)

    for v,k in y:
        print(k,'=',v)

most_frequent()
