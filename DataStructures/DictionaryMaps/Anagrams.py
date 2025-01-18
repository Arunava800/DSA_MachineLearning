"""
Given a list of strings, group the anagrams together.
Example: [eat, tea, tan, ate, nat, bat]
Output: [eat, tea, ate], [tan, nat], [bat]
"""


from typing import List


class Solution:
    @staticmethod
    def calculate_hash_str(freq: List[int]) -> str:
        str_freq = [str(num) for num in freq]
        s = "$".join(str_freq)
        print(s)
        return s

    @staticmethod
    def calculate_freq_arr(word: str) -> List[int]:
        freq = [0 for _ in range(26)]
        for i in range(len(word)):
            freq[ord(word[i]) - ord('a')] += 1
        return freq

    def anagram(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hash_table = dict()
        for word in strs:
            freq_arr = self.calculate_freq_arr(word)
            hash_str = self.calculate_hash_str(freq_arr)
            if hash_table.get(hash_str, None):
                hash_table[hash_str].append(word)
            else:
                hash_table[hash_str] = [word]
        for values in hash_table.values():
            ans.append(values)
        return ans


if __name__ == "__main__":
    anagrams = Solution()
    print(anagrams.anagram(["eat", "ate", "tan", "nat", "ant", "bat"]))
