from collections import defaultdict
word_dict = {}
input  =   ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
min_dist = float("inf")
pair = []
for i  in range(len(input)):
    if input[i] in word_dict:
        if i - word_dict[input[i]] < min_dist:
            min_dist = i - word_dict[input[i]]
            pair = [input[i],min_dist]
    word_dict[input[i]] =i

print(pair)










"""input  =   ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
uniq_words =set(input)
min_dist = float('inf')
word_pair = ['',0]
for word in uniq_words:
    for left in range(len(input)):
        if input[left] == word:
            break
    for right in range(left+1, len(input)):
        if input[right] == word:
            if min_dist > right -left:
                min_dist = right - left
                word_pair = [input[right],min_dist]
            left = right"""
