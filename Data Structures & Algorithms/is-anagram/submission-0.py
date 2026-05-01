class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count= [0]*26
        for i in s:
            letter_count[ord(i.lower()) - ord('a')] += 1
        for j in t:
            letter_count[ord(j.lower()) - ord('a')] -= 1
        return all(count == 0 for count in letter_count)