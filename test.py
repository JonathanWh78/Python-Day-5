from operator import contains


class super:
    def __init__(self, check = ["",""]):
        self.check = check

    def testv(input):
        vowellst = len(vowel)
        if input in vowel:
            result = "True"
            return result

#vowel = ["a","e"]
vowel = ["a","e"]
quick = input("enter e or a: ")
ans = super.testv(quick)
if ans == "True":
    print("this is an idea")