def getter():
    word_list = []
    input = raw_input("Enter line: ")
    while input !="":
        input_list = input.split()
        for item in input_list:
            word_list.append(item)
        input = raw_input("Enter line: ")
    word_list.sort()
    return word_list

def counter(word_list):
    words = list(set(word_list))
    words.sort()
    count_list = []
    for item in words:
        count_list.append(word_list.count(item))
    return count_list

words =  getter()
count_list = counter(words)
words = list(set(words))
words.sort()
for i in range(len(count_list)):
    print words[i], count_list[i]