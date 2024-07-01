from collections import defaultdict
def groupAnagrams(strs: list) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        print(count)
        res[tuple(count)].append(s)
    return res.values()
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
