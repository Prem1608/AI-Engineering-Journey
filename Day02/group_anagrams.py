def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = {}
    for word in strs:
        count = [0]*26
        for ch in word:
            index = ord(ch)-ord("a")
            count[index]+=1
        count = tuple(count)
        if count not in result:
            result[count]=[word]
        else:
            result[count].append(word)
    return list(result.values())