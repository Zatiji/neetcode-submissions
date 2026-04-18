class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        taken = {}
        sortedWords = []

        for word in strs:
            sortedWords.append(sorted(word))
        

        for i in range(len(strs)):
            word1 = strs[i]

            if word1 in taken:
                continue

            partialAnswer = []
            partialAnswer.append(word1)
            taken[word1] = 1

            for j in range(i + 1, len(strs)):
                word2 = strs[j]

                if word1 == word2:
                    partialAnswer.append(word2)
                    continue
                if word2 in taken:
                    continue

                if sortedWords[i] == sortedWords[j]:
                    taken[word2] = 1
                    partialAnswer.append(word2)
            
            answer.append(partialAnswer)
        
        return answer


            
                        


                