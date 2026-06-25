class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for email in emails:
            correct = ""
            am = False
            i = 0

            while i < len(email):
                char = email[i]
                if not am:
                    if char == ".":
                        i+=1
                        continue
                    elif char == "+":
                        while i < len(email) and char != "@":
                            i+=1
                            char = email[i] 
                        am = True
                    elif char == "@":
                        am = True
                correct+=char
                i+=1
            uniques.add(correct)
            
        return len(uniques)