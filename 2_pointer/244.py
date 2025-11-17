from typing import List, Dict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.pos ={}
        for i, w in enumerate(wordsDict):
            self.pos.setdefault(w,[]).append(i) 

    def shortest(self, word1: str, word2: str) -> int:
        a = self.pos.get(word1, [])
        b = self.pos.get(word2, [])
        if not a or not b:
            return -1
        i,j = 0,0
        ans = float('inf')
        while i < len(a) and j < len(b):
            ans = min(ans, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i +=1
            else:
                j +=1
        return ans
        
# get the list of positions for word1 or an empty list if missing

if __name__ == "__main__":
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    wordDistance = WordDistance(wordsDict)
    print(wordDistance.shortest("coding", "practice"))  # Expected output: 3
    print(wordDistance.shortest("makes", "coding"))     # Expected output: 1
    print(wordDistance.shortest("makes", "practice")) 
    print(wordDistance.shortest("perfect", "practice")) 
    print(wordDistance.shortest("makes", "time")) 