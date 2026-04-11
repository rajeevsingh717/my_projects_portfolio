"""
- Letter: "hello", Magazine: "hello world" → True (all characters in the letter can be found in the magazine)       
- Letter: "aab", Magazine: "ab" → False (letter needs two as but magazine only has one)  
- Letter: "attack", Magazine: "cat and a track" → True
"""
from collections import Counter

def is_construct(letter, magazine ):
    let_count = Counter(letter)
    reamining = len(let_count)
    for char in magazine:
        let_count[char] -= 1
        if let_count[char] == 0:
            reamining -= 1
        if reamining == 0:
            return True

    return False
    

print(is_construct("hello", "hello world")) # True
print(is_construct("aab", "ab")) #False
print(is_construct("attack", "cat and a track")) #True
