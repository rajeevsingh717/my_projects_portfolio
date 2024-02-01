"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        new = []
        for i in range(0,len(chars)):
            if i+1 < len(chars) and chars[i] == chars[i+1]:
                count += 1
            else:
                new.append([chars[i],count])
                count = 1
        
        
        i=0
        print(len(new))
        for k,v in new:
            print(k,v)
            
            chars[i]=k
            print(i, k)
            i += 1
            if v>1:
                for item in str(v):
                    chars[i]=str(item)
                    i+=1
            
        return i
