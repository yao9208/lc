class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        match = [0 for x in range(10)]
        bull, cow = 0, 0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull += 1
            else:
                numSecret = int(secret[i])
                numGuess = int(guess[i])
                if match[numSecret]<0:
                    cow += 1
                if match[numGuess]>0:
                    cow += 1
                match[numSecret] += 1
                match[numGuess] -= 1
        return str(bull)+"A"+str(cow)+"B"
