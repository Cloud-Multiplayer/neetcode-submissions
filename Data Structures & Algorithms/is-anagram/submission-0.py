class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstSorted = "".join(sorted(s))
        secondSorted = "".join(sorted(t))
        if firstSorted == secondSorted:
            return True
        else:
            return False
        