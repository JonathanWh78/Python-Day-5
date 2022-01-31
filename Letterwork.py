# Lettercheck
# - write a class called 'Lettercheck'
# - create an attribute called vowels and fill it with vowels
# - create a method that takes a single letter and checks if it is a vowel
# - return true or false
# - rewrite the class so you can create different objects for finding if letters are members of different letter groups


#Class to check if its a vowel
#Re-written with default values
#could add a check instead and pass a list to the __init__ and then just check if an item is in the list
class lettercheck:
    def __init__(self,ISVowel = False, ISRoman = False):
        self.ISVowel = ISVowel
        self.ISRoman = ISRoman

    def newcheckV(UInput):
        vowellst = ["A","E","I","O","U"]
        if UInput in vowellst:
            outputv = "vowel"
            return outputv

    def newcheckR(UInput):
        romanlst = ["I","V","X","L","C","D","M"]
        if UInput in romanlst:
            outputR = "roman"
            return outputR

#Objects
I = lettercheck(True, True)
vowel = lettercheck(True, False)
roman = lettercheck(False, True)
other = lettercheck()

#loop to make more fun
#added roman numeral checks
UInput = str
while UInput != "QUIT":
    print ("-----------------------------------------------------------")
    print ("")
    print ("Enter A Letter, Any Letter You Want!")
    print ("If You Want To Quit Type: Quit")
    print ("")
    UInput = str(input ("Enter A Letter You Want To Check If It's A Vowel Or Roman Numeral: ").upper())

    if UInput == "QUIT":
        print ("")
        print ("---------------------------")
        print ("Quiting, Thanks For Playing")
        print ("---------------------------")        
        print ("")
        exit()
    if UInput == "I":
        print ("")
        print ("-------------------------------------------------------")
        print ("Vowel Check Is: " + str(I.ISVowel) + " - For: " + str(UInput))
        print ("Roman Numeral Check Is: " + str(I.ISRoman) + " - For: " + str(UInput))
        print ("-------------------------------------------------------")
        print ("")
    else:
        if lettercheck.newcheckV(UInput) == "vowel":
            print ("")
            print ("-------------------------------------------------------")
            print ("Vowel Check Is: " + str(vowel.ISVowel) + " - For: " + str(UInput))
            print ("Roman Numeral Check Is: " + str(vowel.ISRoman) + " - For: " + str(UInput))
            print ("-------------------------------------------------------")
            print ("")
        elif lettercheck.newcheckR(UInput) == "roman":
            print ("")
            print ("-------------------------------------------------------")
            print ("Vowel Check Is: " + str(roman.ISVowel) + " - For: " + str(UInput))
            print ("Roman Numeral Check Is: " + str(roman.ISRoman) + " - For: " + str(UInput))
            print ("-------------------------------------------------------")
            print ("")
        else:
            print ("")
            print ("-------------------------------------------------------")
            print ("Vowel Check Is: " + str(other.ISVowel) + " - For: " + str(UInput))
            print ("Roman Numeral Check Is: " + str(other.ISVowel) + " - For: " + str(UInput))
            print ("-------------------------------------------------------")
            print ("")