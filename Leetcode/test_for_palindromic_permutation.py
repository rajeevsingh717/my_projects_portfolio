from collections import defaultdict, Counter
def test_palin_perm(word):
    char_count = Counter(word)
    return True if sum(value%2 for value in char_count.values()) <=1 else False



print(test_palin_perm('racecar')) # true
print(test_palin_perm('aab')) # true
print(test_palin_perm('code')) # false


"""
def test_palin_perm(word):
    char_dict = defaultdict(int)
    word_len = len(word)

    for char in word:
         char_dict[char] = char_dict[char] + 1
    
    all_sum = sum(v % 2 for k,v in char_dict.items())
    if all_sum <= 1:
         return True
    else:
         return False
"""
