class Solution:
    """
         Word should be lower or upper or first letter should be Capital
         

    """
    def detectCapitalUse(self, word: str) -> bool:

        return True if word.isupper() or word.islower() or word == word.capitalize() else False
    def is_capital(self, letter):
        return letter.upper() == letter


print(Solution().detectCapitalUse('LEetcode'))#false

print(Solution().detectCapitalUse('Leetcode'))#True

